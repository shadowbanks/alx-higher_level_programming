#!/usr/bin/python3
"""Module Documentation"""
import urllib.request
import sys


def main():
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))


if __name__ == '__main__':
    main()
