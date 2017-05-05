#!/usr/bin/env python

#
# scanless.py
# main program
#

import argparse
from modules import viewdns


def scanless(target):
    print('Running scanless...\n')
    viewdns.scan(target)


def get_parser():
    parser = argparse.ArgumentParser(description='scanless, public port scan scrapper')
    parser.add_argument('-t', '--target', help='ip or domain to scan',
                        required=True, type=str)
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    target = args['target']

    scanless(target)


if __name__ == '__main__':
    main()
