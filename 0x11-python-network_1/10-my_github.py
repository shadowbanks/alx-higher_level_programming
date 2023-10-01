#!/usr/bin/python3
"""Module Documentation"""
import requests
import sys


def main():
    """Get a Github user's id"""
    bearer = f"Bearer {sys.argv[2]}"
    headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": bearer
            }
    url = f"https://api.github.com/users/{sys.argv[1]}"
    req = requests.get(url, headers=headers)
    status = req.status_code
    if status == 200:
        data = req.json()
        print(data.get("id"))
    else:
        print("None")


if __name__ == "__main__":
    main()
