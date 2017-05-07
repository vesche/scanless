#
# scanless yougetsignal module
# https://github.com/vesche/scanless
#

import bs4
import requests

BASE_URL = 'http://ports.yougetsignal.com'
SCAN_LOC = '/short-scan.php'
OUTPUT = '''
------- yougetsignal -------
PORT     STATE  SERVICE
21/tcp   {:<6} ftp
22/tcp   {:<6} ssh
23/tcp   {:<6} telnet
25/tcp   {:<6} smtp
53/tcp   {:<6} dns
80/tcp   {:<6} http
110/tcp  {:<6} pop3
115/tcp  {:<6} sftp
135/tcp  {:<6} msrpc
139/tcp  {:<6} netbios
143/tcp  {:<6} imap
194/tcp  {:<6} irc
443/tcp  {:<6} https
445/tcp  {:<6} smb
1433/tcp {:<6} mssql
3306/tcp {:<6} mysql
3389/tcp {:<6} rdp
5632/tcp {:<6} pcanywhere
5900/tcp {:<6} vnc
6112/tcp {:<6} wc3
----------------------------'''


def scan(target):
    url = '{}{}'.format(BASE_URL, SCAN_LOC)

    payload = { 'remoteAddress': target }
    r = requests.post(url, payload)

    page = r.content
    soup = bs4.BeautifulSoup(page, 'html.parser')
    imgs = soup.findAll('img')

    status = []
    for i in imgs:
        i = str(i)

        if 'flag_red.gif' in i:
            status.append('closed')
        else:
            status.append('open')

    return OUTPUT.format(*status)
