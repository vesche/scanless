# -*- coding: utf-8 -*-

#
# scanless standingtech module
# https://github.com/vesche/scanless
#

import requests

BASE_URL = 'https://portscanner.standingtech.com/'
SCAN_LOC = '/portscan.php?port={}&host={}'
OUTPUT = '''
------- standingtech -------
PORT     STATE  SERVICE
21/tcp   {:<6} ftp
22/tcp   {:<6} ssh
23/tcp   {:<6} telnet
25/tcp   {:<6} smtp
80/tcp   {:<6} http
110/tcp  {:<6} pop3
139/tcp  {:<6} netbios
143/tcp  {:<6} imap
443/tcp  {:<6} https
445/tcp  {:<6} smb
1433/tcp {:<6} mssql
3306/tcp {:<6} mysql
3389/tcp {:<6} rdp
5900/tcp {:<6} vnc
----------------------------'''
PORTS = [21, 22, 23, 25, 80, 110, 139, 143, 443, 445, 1433, 3306, 3389, 5900]


def scan(target):
    url = '{}{}'.format(BASE_URL, SCAN_LOC)

    status = []
    for port in PORTS:
        r = requests.get(url.format(port, target))
        page = str(r.content)

        if 'open' in page:
            status.append('open')
        else:
            status.append('closed')

    return OUTPUT.format(*status)
