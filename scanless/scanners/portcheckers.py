#
# scanless portcheckers module
# https://github.com/vesche/scanless
#

import requests

BASE_URL = 'http://www.portcheckers.com'
SCAN_LOC = '/portscan-result'
OUTPUT = '''
-------- portcheckers --------
PORT     STATE  SERVICE
21/tcp   {:<6} ftp
22/tcp   {:<6} ssh
23/tcp   {:<6} telnet
25/tcp   {:<6} smtp
80/tcp   {:<6} http
110/tcp  {:<6} pop3
115/tcp  {:<6} sftp
143/tcp  {:<6} imap
443/tcp  {:<6} https
1433/tcp {:<6} ms-sql-s
3306/tcp {:<6} mysql
3389/tcp {:<6} ms-wbt-server
5900/tcp {:<6} rfb
8080/tcp {:<6} webcache
-----------------------------'''


def scan(target):
    url = '{}{}'.format(BASE_URL, SCAN_LOC)

    payload = { 'server': target, 'quick': 'true' }
    r = requests.post(url, payload)

    page = str(r.content)
    pagelist = page.split('<div><span style="display: inline-block;width:200px;">')[1:]

    status = []
    for i in pagelist:
        i = str(i)

        if 'Open' in i:
            status.append('open')
        elif 'Not Available' in i:
            status.append('closed')
        else:
            status.append('error')

    return OUTPUT.format(*status)
