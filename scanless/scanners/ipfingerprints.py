#
# scanless ipfingerprints module
# https://github.com/vesche/scanless
#

import re
import requests

BASE_URL = 'http://www.ipfingerprints.com'
SCAN_LOC = '/scripts/getPortsInfo.php'
OUTPUT = '''
------- ipfingerprints -------
{}
------------------------------'''


def scan(target):
    url = '{}{}'.format(BASE_URL, SCAN_LOC)

    payload = { 'remoteHost': target,
                'start_port': 20,
                'end_port': 512,
                'normalScan': 'No',
                'scan_type': 'connect',
                'ping_type': 'none',
                'os_detect': 'on' }
    r = requests.post(url, payload)

    page = r.content.decode('utf-8')
    page = re.sub('<[^<]+?>', '', page)
    page = page.replace('\\n','\n').replace('\\/','/')[36:-46]

    return OUTPUT.format(page)
