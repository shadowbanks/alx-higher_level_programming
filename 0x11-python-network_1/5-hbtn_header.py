#!/usr/bin/python3
"""Module Documentation"""
import requests
import sys


def main():
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))


if __name__ == '__main__':
    main()
