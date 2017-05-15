#!/usr/bin/env python

#
# scanless - public port scan scrapper
# https://github.com/vesche/scanless
#

import argparse
import sys

try:
    from scanners import *
except:
    print('Error, scanless requires the requests and bs4 libraries.')
    sys.exit(1)


SCAN_LIST = '''Scanner Name   | Website
---------------|------------------------------
yougetsignal   | http://www.yougetsignal.com
viewdns        | http://viewdns.info
hackertarget   | https://hackertarget.com
ipfingerprints | http://www.ipfingerprints.com
pingeu         | http://ping.eu
spiderip       | https://spiderip.com
portcheckers   | http://www.portcheckers.com
t1shopper      | http://www.t1shopper.com
shodanip       | https://www.shodan.io/
'''
SCANNERS = { 'yougetsignal':     yougetsignal,
             'viewdns':          viewdns,
             'hackertarget':     hackertarget,
             'ipfingerprints':   ipfingerprints,
             'pingeu':           pingeu,
             'spiderip':         spiderip,
             'portcheckers':     portcheckers,
             't1shopper':        t1shopper,
             'shodanip':         shodanip}


def scanless(target, scanner):
    def run(s):
        try:
            return SCANNERS[s].scan(target)
        except Exception as e:
            # return 'Error, {} was unable to run.'.format(s)
            raise e

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
    parser.add_argument('-t', '--target', help='ip or domain to scan',
                        type=str)
    parser.add_argument('-s', '--scanner', help='scanner to use (default: yougetsignal)',
                        type=str, default='yougetsignal')
    parser.add_argument('-l', '--list', help='list scanners',
                        action='store_true')
    parser.add_argument('-a', '--all', help='use all the scanners',
                        action='store_true')
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    if args['list']:
        print(SCAN_LIST)
        return

    if not args['target']:
        parser.print_help()
        return

    target = args['target']
    scanner = args['scanner'].lower()

    if args['all']:
        scanner = 'all'

    scanless(target, scanner)


if __name__ == '__main__':
    main()
