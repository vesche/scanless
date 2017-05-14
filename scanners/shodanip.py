#
# scanless shodan module
# https://github.com/vesche/scanless
#

import shodan
import socket
from conf import config

OUTPUT = """
------- shodan -------
PORT     STATE
{}
----------------------
"""


def scan(target):
    try:
        if config.shodan_key:
            api = shodan.Shodan(config.shodan_key)
            host = api.host(socket.gethostbyname(target))
            return OUTPUT.format(''.join(['{:8}{}'.format(str(host), ' open\n')
                                          for host in host['ports']]))
        return 'Shodan API key missing'
    except (shodan.exception.APIError, socket.error):
        pass
