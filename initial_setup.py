#!/usr/bin/env python3

import argparse
from tqdm import tqdm


parser = argparse.ArgumentParser(
        prog='initial_setup.py',
        usage='Initial setup script.',
        description='Setup and configuration for bash, vim, and others.',
        add_help=True
        )

parser.add_argument(
        '--os',
        '-o',
        choices=['redhat','ubuntu'],
        nargs=1,
        required=True,
        help='Specify the Operation System.'
        )

args = parser.parse_args()

class Package_install(object):

    def __init__(self, json_conf):
        pass

    def yum_install(package_list):
        pass

    def pip_install(pip_list):
        pass

    def npm_install(npm_list):
        pass


def main():
    pass

if __name__ == '__main__':
    main()
