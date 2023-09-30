#!/usr/bin/python3
"""Module Documentation"""
import requests
import sys


def main():
    r = requests.get(sys.argv[1])
    statusCode = r.status_code
    if statusCode >= 400:
        print('Error code: {}'.format(statusCode))
    else:
        print(r.text)


if __name__ == '__main__':
    main()
