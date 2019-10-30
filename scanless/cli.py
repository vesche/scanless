"""scanless.cli"""

import argparse

from random import choice
from scanless.core import Scanless

SCAN_LIST = '''\
+----------------+--------------------------------------+
| Scanner Name   | Website                              |
+----------------|--------------------------------------+
| hackertarget   | https://hackertarget.com             |
| ipfingerprints | https://www.ipfingerprints.com       |
| pingeu         | https://ping.eu                      |
| spiderip       | https://spiderip.com                 |
| standingtech   | https://portscanner.standingtech.com |
| t1shopper      | http://www.t1shopper.com             |
| viewdns        | https://viewdns.info                 |
| yougetsignal   | https://www.yougetsignal.com         |
+----------------+--------------------------------------+'''
VERSION = '2.0.0'

sl = Scanless()


def get_parser():
    parser = argparse.ArgumentParser(
        description='scanless, an online port scan scraper.'
    )
    parser.add_argument(
        '-v', '--version',
        action='store_true', help='display the current version'
    )
    parser.add_argument(
        '-t', '--target',
        help='ip or domain to scan', type=str
    )
    parser.add_argument(
        '-s', '--scanner',
        default='hackertarget',
        help='scanner to use (default: hackertarget)', type=str
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
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    if args['version']:
        print(f'v{VERSION}'); return
    if args['list']:
        print(SCAN_LIST); return
    if not args['target']:
        parser.print_help(); return

    target = args['target']
    scanner = args['scanner'].lower()

    print(f'Running scanless v{VERSION}...')
    scanners = sl.scanners.keys()

    if args['all']:
        for s in scanners:
            print(f'{s}:')
            print(sl.scan(target, scanner=s) + '\n')
        return

    if args['random']:
        scanner = choice(list(scanners))

    if scanner in scanners:
        print(f'{scanner}:')
        print(sl.scan(target, scanner=scanner))
    else:
        print('Scanner not found, see --list to view all supported scanners.')
