#!/usr/bin/env python

#
# scanless.py
# main program
#

import argparse
from modules import viewdns, hackertarget

SCANNERS = '''
Scanner Name | Website
-------------|--------------------------
viewdns      | http://viewdns.info/
hackertarget | https://hackertarget.com/
'''


def scanless(target, scanner):
    print('Running scanless...')

    if scanner == 'all':
        return viewdns.scan(target) + hackertarget.scan(target)
    elif scanner == 'viewdns':
        return viewdns.scan(target)
    elif scanner == 'hackertarget':
        return hackertarget.scan(target)
    else:
        return 'Scanner not found, see --list to view all.'


def get_parser():
    parser = argparse.ArgumentParser(description='scanless, public port scan scrapper')
    parser.add_argument('-t', '--target', help='ip or domain to scan',
                        type=str)
    parser.add_argument('-s', '--scanner', help='scanner to use (default: viewdns)',
                        type=str, default='viewdns')
    parser.add_argument('-l', '--list', help='list scanners',
                        action='store_true')
    parser.add_argument('-a', '--all', help='use all the scanners',
                        action='store_true')
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    if args['list']:
        print(SCANNERS)
        return

    if not args['target']:
        parser.print_help()
        return

    target = args['target']
    scanner = args['scanner'].lower()

    if args['all']:
        scanner = 'all'

    print(scanless(target, scanner))


if __name__ == '__main__':
    main()
