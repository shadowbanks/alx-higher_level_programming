#!/usr/bin/python3
"""Module Documentation"""
import requests
import sys


def main():
    value = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=value)
    print(r.text)


if __name__ == '__main__':
    main()
