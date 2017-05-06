#!/usr/bin/env python

#
# scanless - public port scan scrapper
# https://github.com/vesche/scanless
#

import argparse
from modules import viewdns, hackertarget, yougetsignal

SCANNERS = '''Scanner Name | Website
-------------|-----------------------------
yougetsignal | http://www.yougetsignal.com/
viewdns      | http://viewdns.info/
hackertarget | https://hackertarget.com/
'''


def scanless(target, scanner):
    print('Running scanless...')

    if scanner == 'all':
        print(yougetsignal.scan(target))
        print(viewdns.scan(target))
        print(hackertarget.scan(target))
    elif scanner == 'viewdns':
        print(viewdns.scan(target))
    elif scanner == 'hackertarget':
        print(hackertarget.scan(target))
    elif scanner == 'yougetsignal':
        print(yougetsignal.scan(target))
    else:
        return 'Scanner not found, see --list to view all supported scanners.'


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
        print(SCANNERS)
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
