#!/usr/bin/python3
"""Module Documentation"""
import urllib.request
import sys


def main():
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == '__main__':
    main()
