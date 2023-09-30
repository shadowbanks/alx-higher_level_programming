#!/usr/bin/python3
"""Module Documentation"""
import sys
import requests


def main():
    send = {"q": ""}
    if len(sys.argv) == 2:
        send["q"] = sys.argv[1]

    r = requests.post('http://0.0.0.0:5000/search_user', send)
    try:
        result = r.json()
        if result == {}:
            print("No result")
        else:
            print("[{}] {}".format(result["id"], result["name"]))
    except ValueError:
        print("Not a valid JSON")


if __name__ == '__main__':
    main()
