#!/usr/bin/python3
"""Module Documentation"""
import urllib.request
import urllib.parse
import sys


def main():
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    req.method = 'POST'
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))


if __name__ == '__main__':
    main()
