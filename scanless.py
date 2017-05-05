#!/usr/bin/env python

#
# scanless.py
# main program
#

import argparse
from modules import viewdns

SCANNERS = ['viewdns - http://viewdns.info/']


def scanless(target):
    print('Running scanless...')
    viewdns.scan(target)


def get_parser():
    parser = argparse.ArgumentParser(description='scanless, public port scan scrapper')
    parser.add_argument('-l', '--list',   help='list scanners', action='store_true')
    parser.add_argument('-t', '--target', help='ip or domain to scan', type=str)
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    if args['list']:
        print('Scanner   Website')
        print('\n'.join(SCANNERS) + '\n')
        return

    if not args['target']:
        parser.print_help()
        return

    target = args['target']
    scanless(target)


if __name__ == '__main__':
    main()
