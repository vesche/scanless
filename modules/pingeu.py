#
# scanless pingeu module
# https://github.com/vesche/scanless
#

import requests

BASE_URL = 'http://ping.eu'
SCAN_LOC = '/action.php?atype=5'
OUTPUT = '''
------- pingeu -------
PORT     STATE  SERVICE
21/tcp   {:<6} ftp
22/tcp   {:<6} ssh
23/tcp   {:<6} telnet
25/tcp   {:<6} smtp
53/tcp   {:<6} dns
80/tcp   {:<6} http
139/tcp  {:<6} netbios
443/tcp  {:<6} https
445/tcp  {:<6} smb
3389/tcp {:<6} rdp
----------------------'''
PORTS = [ '21', '22', '23', '25', '53', '80', '139', '443', '445', '3389' ]


def scan(target):
    url = '{}{}'.format(BASE_URL, SCAN_LOC)

    state = []
    for p in PORTS:
        payload = { 'host': 'scanme.nmap.org',
                    'port': p,
                    'go': 'Go' }
        r = requests.post(url, payload)
        results = str(r.content)

        if 'closed' in results:
            state.append('closed')
        # ping.eu only allows 10 requests per minute
        elif '10 requests per minute' in results:
            state.append('error')
        else:
            state.append('open')

    return OUTPUT.format(*state)
