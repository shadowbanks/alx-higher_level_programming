#!/usr/bin/python3
import urllib.request

""" Get the status"""


def main():
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print(f"Body response:\n\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")


if '__main__' == __name__:
    main()
