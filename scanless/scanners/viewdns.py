#
# scanless viewdns module
# https://github.com/vesche/scanless
#

import bs4
import requests

BASE_URL = 'http://viewdns.info'
SCAN_LOC = '/portscan/?host='
OUTPUT = '''
------- viewdns -------
PORT     STATE  SERVICE
21/tcp   {:<6} ftp
22/tcp   {:<6} ssh
23/tcp   {:<6} telnet
25/tcp   {:<6} smtp
53/tcp   {:<6} dns
80/tcp   {:<6} http
110/tcp  {:<6} pop3
139/tcp  {:<6} netbios
143/tcp  {:<6} imap
443/tcp  {:<6} https
445/tcp  {:<6} smb
1433/tcp {:<6} mssql
1521/tcp {:<6} oracle
3306/tcp {:<6} mysql
3389/tcp {:<6} rdp
-----------------------'''


def scan(target):
    url = '{}{}{}'.format(BASE_URL, SCAN_LOC, target)

    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.text, 'html.parser')

    table = soup.find('table')
    rows = soup.findAll('tr')

    status = []
    for tr in rows[7:22]:
        cols = str(tr.findAll('td'))

        if 'error.GIF' in cols:
            status.append('closed')
        else:
            status.append('open')

    return OUTPUT.format(*status)
