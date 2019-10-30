"""scanless.core"""

import os
import re
import bs4
import requests

from random import choice
from scanless.exceptions import ScannerNotFound, ScannerRequestError

URL_HACKERTARGET    = 'https://hackertarget.com/nmap-online-port-scanner/'
URL_IPFINGERPRINTS  = 'https://www.ipfingerprints.com/scripts/getPortsInfo.php'
URL_PINGEU          = 'https://ping.eu/action.php?atype=5'
URL_SPIDERIP        = 'https://spiderip.com/inc/port_scan.php'
URL_STANDINGTECH    = 'https://portscanner.standingtech.com/portscan.php?port={0}&host={1}&protocol=TCP'
URL_T1SHOPPER       = 'http://www.t1shopper.com/tools/port-scan/result/'
URL_VIEWDNS         = 'https://viewdns.info/portscan/?host={0}'
URL_YOUGETSIGNAL    = 'https://ports.yougetsignal.com/short-scan.php'

pwd = os.path.abspath(os.path.dirname(__file__))
nmap_file = os.path.join(pwd, 'static/nmap-services.txt')
ua_file = os.path.join(pwd, 'static/user-agents.txt')
NMAP_SERVICES = open(nmap_file, 'r').read().splitlines()
USER_AGENTS = open(ua_file, 'r').read().splitlines()

OUTPUT_TEMPLATE = '''PORT      STATE  SERVICE\n{lines}'''


def lookup_service(port):
    for line in NMAP_SERVICES:
        if f'{port}/tcp' in line:
            return line.split()[0]


def generate_output(raw_data):
    # raw_data = [(22, 'closed'), (23, 'open'), ...]
    lines = []
    for raw in raw_data:
        p, state = raw
        service = lookup_service(p)
        port = f'{p}/tcp'
        lines.append(f'{port:<9} {state:<6} {service}')
    return OUTPUT_TEMPLATE.format(lines='\n'.join(lines))


class Scanless:
    def __init__(self):
        self.session = requests.Session()
        self.scanners = {
            'hackertarget':    self.hackertarget,
            'ipfingerprints':  self.ipfingerprints,
            'pingeu':          self.pingeu,
            'spiderip':        self.spiderip,
            'standingtech':    self.standingtech,
            't1shopper':       self.t1shopper,
            'viewdns':         self.viewdns,
            'yougetsignal':    self.yougetsignal,
        }

    def scan(self, target, scanner='hackertarget'):
        if scanner not in self.scanners:
            raise ScannerNotFound(f'Unknown scanner, {scanner}.')
        return self.scanners[scanner](target)

    def _request(self, url, payload=None, method='POST'):
        self._randomize_user_agent()
        try:
            response = self.session.request('POST', url, data=payload)
        except Exception as e:
            raise ScannerRequestError(e)
        response.raise_for_status()
        return response.content.decode('utf-8')

    def _randomize_user_agent(self):
        self.session.headers['User-Agent'] = choice(USER_AGENTS)

    def hackertarget(self, target):
        payload = {
            'theinput': target,
            'thetest': 'nmap',
            'name_of_nonce_field': '5a8d0006b9',
            '_wp_http_referer': '/nmap-online-port-scanner/'
        }
        scan_results = self._request(URL_HACKERTARGET, payload)
        soup = bs4.BeautifulSoup(scan_results, 'html.parser')
        output = soup.findAll('pre', {'id': 'formResponse'})[0].string
        return output.replace('\\n', '\n').strip()

    def ipfingerprints(self, target):
        payload = {
            'remoteHost': target,
            'start_port': 20,
            'end_port': 512,
            'normalScan': 'No',
            'scan_type': 'connect',
            'ping_type': 'none',
            'os_detect': 'on'
        }
        scan_results = self._request(URL_IPFINGERPRINTS, payload)
        output = re.sub('<[^<]+?>', '', scan_results)
        return output.replace('\\n','\n').replace('\\/','/')[36:-46].strip()

    def pingeu(self, target):
        ports = [
            '21', '22', '23', '25', '53', '80', '139', '443', '445', '3389'
        ]
        raw_data = []
        for p in ports:
            payload = {'host': target, 'port': p, 'go': 'Go'}
            result = self._request(URL_PINGEU, payload)
            if 'closed' in result:
                raw_data.append((p, 'closed'))
            elif '10 requests per minute' in result:
                raw_data.append((p, 'error')) 
            else:
                raw_data.append((p, 'open'))
        return generate_output(raw_data)

    def spiderip(self, target):
        ports = [
            21, 22, 25, 80, 110, 143, 443, 465, 993, 995, 1433, 3306, 3389,
            5900, 8080, 8443
        ]
        payload = {'ip': target, 'language[]': ports}
        scan_results = self._request(URL_SPIDERIP, payload).split('/images/')
        scan_results.pop(0)
        raw_data = []
        for result, port in zip(scan_results, ports):
            if 'open' in result:
                raw_data.append((port, 'open'))
            else:
                raw_data.append((port, 'closed'))
        return generate_output(raw_data)

    def standingtech(self, target):
        ports = [
            21, 22, 23, 25, 80, 110, 139, 143, 443, 445, 1433, 3306, 3389, 5900
        ]
        raw_data = []
        for p in ports:
            result = self._request(
                URL_STANDINGTECH.format(p, target),
                method='GET'
            )
            if 'open' in result:
                raw_data.append((p, 'open'))
            else:
                raw_data.append((p, 'closed'))
        return generate_output(raw_data)

    def t1shopper(self, target):
        ports = [
            21, 23, 25, 80, 110, 139, 445, 1433, 1521, 1723, 3306, 3389,
            5900, 8080
        ]
        payload = {'scan_host': target, 'port_array[]': ports}
        scan_results = self._request(URL_T1SHOPPER, payload)
        soup = bs4.BeautifulSoup(scan_results, 'html.parser')
        raw_data = []
        for tt, port in zip(soup.find('pre').find_all('tt'), ports):
            if tt.text.find('isn\'t') > -1:
                raw_data.append((port, 'closed'))
            else:
                raw_data.append((port, 'open'))
        return generate_output(raw_data)

    def viewdns(self, target):
        ports = [
            21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 1433, 1521,
            3306, 3389
        ]
        scan_results = self._request(URL_VIEWDNS.format(target), method='GET')
        soup = bs4.BeautifulSoup(scan_results, 'html.parser')
        table, rows = soup.find('table'), soup.findAll('tr')
        raw_data = []
        for tr, port in zip(rows[7:22], ports):
            cols = str(tr.findAll('td'))
            if 'error.GIF' in cols:
                raw_data.append((port, 'closed'))
            else:
                raw_data.append((port, 'open'))
        return generate_output(raw_data)

    def yougetsignal(self, target):
        ports = [
            21, 22, 23, 25, 53, 80, 110, 115, 135, 139, 143, 194, 443, 445,
            1433, 3306, 3389, 5632, 5900, 6112
        ]
        payload = {'remoteAddress': target}
        scan_results = self._request(URL_YOUGETSIGNAL, payload)
        soup = bs4.BeautifulSoup(scan_results, 'html.parser')
        imgs = soup.findAll('img')
        raw_data = []
        for img, port in zip(imgs, ports):
            if 'red' in str(img):
                raw_data.append((port, 'closed'))
            else:
                raw_data.append((port, 'open'))
        return generate_output(raw_data)
