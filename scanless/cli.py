"""scanless.cli"""

import crayons
import argparse

from random import choice
from scanless.core import Scanless

SCAN_LIST = '''\
+----------------+--------------------------------------+
| Scanner Name   | Website                              |
+----------------+--------------------------------------+
| hackertarget   | https://hackertarget.com             |
| ipfingerprints | https://www.ipfingerprints.com       |
| pingeu         | https://ping.eu                      |
| spiderip       | https://spiderip.com                 |
| standingtech   | https://portscanner.standingtech.com |
| t1shopper      | http://www.t1shopper.com             |
| viewdns        | https://viewdns.info                 |
| yougetsignal   | https://www.yougetsignal.com         |
+----------------+--------------------------------------+'''
VERSION = '2.1.3'

sl = Scanless(cli_mode=True)


def get_parser():
    parser = argparse.ArgumentParser(
        description='scanless, an online port scan scraper.'
    )
    parser.add_argument(
        '-v', '--version',
        action='store_true',
        help='display the current version'
    )
    parser.add_argument(
        '-t', '--target',
        help='ip or domain to scan',
        type=str
    )
    parser.add_argument(
        '-s', '--scanner',
        default='hackertarget',
        help='scanner to use (default: hackertarget)',
        type=str
    )
    parser.add_argument(
        '-r', '--random',
        action='store_true',
        help='use a random scanner'
    )
    parser.add_argument(
        '-l', '--list',
        action='store_true',
        help='list scanners'
    )
    parser.add_argument(
        '-a', '--all',
        action='store_true',
        help='use all the scanners'
    )
    parser.add_argument(
        '-d', '--debug',
        action='store_true',
        help='debug mode (cli mode off & show network errors)'
    )
    return parser


def display(results):
    for line in results.split('\n'):
        if not line:
            continue
        elif 'tcp' in line or 'udp' in line:
            if 'open' in line:
                line = crayons.green(line)
            elif 'closed' in line:
                line = crayons.red(line)
            elif 'filtered' in line:
                line = crayons.yellow(line)
        print(line)


def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    if args['version']:
        print(f'v{VERSION}')
        return

    if args['list']:
        print(SCAN_LIST)
        return

    if not args['target']:
        parser.print_help()
        return

    if args['debug']:
        sl.cli_mode = False

    target = args['target']
    scanner = args['scanner'].lower()

    print(f'Running scanless v{VERSION}...\n')
    scanners = sl.scanners.keys()

    if args['all']:
        for s in scanners:
            print(f'{s}:')
            display(sl.scan(target, scanner=s)['raw'])
            print()
        return

    if args['random']:
        scanner = choice(list(scanners))

    if scanner in scanners:
        print(f'{scanner}:')
        display(sl.scan(target, scanner=scanner)['raw'])
    else:
        print('Scanner not found, see --list to view all supported scanners.')
