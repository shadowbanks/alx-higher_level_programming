#!/usr/bin/python3
"""Module Documentation"""
import requests


def main():
    r = requests.get('https://alx-intranet.hbtn.io/status')
    data = r.text
    print('Body response:\n\t- type: {}'.format(type(data)))
    print('\t- content: {}'.format(data))


if __name__ == '__main__':
    main()
