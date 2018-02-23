#!/usr/bin/env python

#
# scanless - public port scan scrapper
# https://github.com/vesche/scanless
#

import argparse
import sys
from random import choice

from . import __version__
from .scanners import *


SCAN_LIST = '''Scanner Name   | Website
---------------|------------------------------
yougetsignal   | http://www.yougetsignal.com
viewdns        | http://viewdns.info
hackertarget   | https://hackertarget.com
ipfingerprints | http://www.ipfingerprints.com
pingeu         | http://ping.eu
spiderip       | https://spiderip.com
t1shopper      | http://www.t1shopper.com
'''
SCANNERS = { 'yougetsignal':     yougetsignal,
             'viewdns':          viewdns,
             'hackertarget':     hackertarget,
             'ipfingerprints':   ipfingerprints,
             'pingeu':           pingeu,
             'spiderip':         spiderip,
             't1shopper':        t1shopper }


def scanless(target, scanner):
    def run(s):
        try:
            return SCANNERS[s].scan(target)
        # no error is returned here because it's irrelevant
        except:
            return 'Error, {} was unable to run.'.format(s)

    print('Running scanless...')

    if scanner == 'all':
        for s, _ in SCANNERS.items():
            print(run(s))
    elif scanner in SCANNERS:
        print(run(scanner))
    else:
        print('Scanner not found, see --list to view all supported scanners.')


def get_parser():
    parser = argparse.ArgumentParser(description='scanless, public port scan scrapper')
    parser.add_argument('-v', '--version', help='display the current version',
                        action='store_true')
    parser.add_argument('-t', '--target', help='ip or domain to scan',
                        type=str)
    parser.add_argument('-s', '--scanner', help='scanner to use (default: hackertarget)',
                        type=str, default='hackertarget')
    parser.add_argument('-r', '--random', help='use a random scanner',
                        action='store_true')
    parser.add_argument('-l', '--list', help='list scanners',
                        action='store_true')
    parser.add_argument('-a', '--all', help='use all the scanners',
                        action='store_true')
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    if args['version']:
        print(__version__)
        return

    if args['list']:
        print(SCAN_LIST)
        return

    if not args['target']:
        parser.print_help()
        return

    target = args['target']
    scanner = args['scanner'].lower()

    if args['random']:
        scanner = choice([s for s, _ in SCANNERS.items()])

    if args['all']:
        scanner = 'all'

    scanless(target, scanner)


if __name__ == '__main__':
    main()
