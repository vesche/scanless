"""scanless spiderip module"""

import requests

BASE_URL = 'https://spiderip.com'
SCAN_LOC = '/inc/port_scan.php'
OUTPUT = '''
------- spiderip -------
PORT     STATE  SERVICE
21/tcp   {:<6} ftp
22/tcp   {:<6} ssh
25/tcp   {:<6} smtp
80/tcp   {:<6} http
110/tcp  {:<6} pop3
143/tcp  {:<6} imap
443/tcp  {:<6} https
465/tcp  {:<6} smtps
993/tcp  {:<6} imaps
995/tcp  {:<6} pop3s
1433/tcp {:<6} mssql
3306/tcp {:<6} mysql
3389/tcp {:<6} rdp
5900/tcp {:<6} vnc
8080/tcp {:<6} http-alt
8443/tcp {:<6} https-alt
------------------------'''


def scan(target):
    url = '{}{}'.format(BASE_URL, SCAN_LOC)

    r = requests.post(url, data={'ip': target, 'language[]': [21, 22, 25, 80,
        110, 143, 443, 465, 993, 995, 1433, 3306, 3389, 5900, 8080, 8443]})

    page = str(r.content)
    page_split = page.split('/images/')
    del page_split[0]

    status = []
    for i in page_split:
        i = str(i)

        if 'open' in i:
            status.append('open')
        else:
            status.append('closed')

    return OUTPUT.format(*status)
