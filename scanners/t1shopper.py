#
# scanless spiderip module
# https://github.com/vesche/scanless
#

import requests

from bs4 import BeautifulSoup


BASE_URL = 'http://www.t1shopper.com'
SCAN_LOC = '/tools/port-scan/result/'

OUTPUT = '''
------- t1shopper ------
PORT     STATE  SERVICE
21/tcp   {:<6} ftp
23/tcp   {:<6} telnet
25/tcp   {:<6} smtp
80/tcp   {:<6} http
110/tcp  {:<6} pop3
139/tcp  {:<6} netbios-ssn
445/tcp  {:<6} microsoft-ds
1433/tcp {:<6} ms-sql-s
1521/tcp {:<6} ncube-lm
1723/tcp {:<6} pptp
3306/tcp {:<6} mysql
3389/tcp {:<6} rdp
5900/tcp {:<6} vnc
8080/tcp {:<6} http-alt
------------------------'''


def scan(target):

    url = '{}{}'.format(BASE_URL, SCAN_LOC)

    r = requests.post(url, data={'scan_host': target, 'port_array[]': [21, 23, 25, 80, 110, 139, 445, 1433, 1521, 1723, 3306, 3389, 5900, 8080]})

    soup = BeautifulSoup(r.text, 'html.parser')

    status = []

    for tt in soup.find('pre').find_all('tt'):

        status.append('closed' if tt.text.find('isn\'t') > -1 else 'open')

    return OUTPUT.format(*status)
