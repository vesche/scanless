#
# scanless hackertarget module
# https://github.com/vesche/scanless
#

import bs4
import requests

BASE_URL = 'https://hackertarget.com'
SCAN_LOC = '/nmap-online-port-scanner/'
OUTPUT = '''
------- hackertarget -------
{}
----------------------------'''


def scan(target):
    url = '{}{}'.format(BASE_URL, SCAN_LOC)

    payload = { 'theinput': target,
                'thetest': 'nmap',
                'name_of_nonce_field': '5a8d0006b9',
                '_wp_http_referer': '/nmap-online-port-scanner/' }
    r = requests.post(url, payload)

    page = r.content
    soup = bs4.BeautifulSoup(page, 'html.parser')
    data = soup.findAll('pre', {'id': 'formResponse'})[0].string

    return OUTPUT.format(data[2:-2].replace('\\n', '\n'))
