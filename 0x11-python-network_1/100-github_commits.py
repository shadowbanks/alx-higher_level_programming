#!/usr/bin/python3
"""Module Documentation"""
import sys
import requests


def main():
    """Get the last 10 commits of a user's repo"""
    i = 0
    headers = {"Accept": "application/vnd.github+json"}
    user = sys.argv[2]
    repo = sys.argv[1]
    url = f"https://api.github.com/repos/{user}/{repo}/commits"
    req = requests.get(url, headers=headers)
    status = req.status_code
    if status == 200:
        datas = req.json()
        for data in datas:
            if i == 10:
                break
            print(f"{data.get('sha')}: {data.get('commit')['author']['name']}")
            i += 1
    # else:
    #    print("something went wrong")
    #    print(status)


if __name__ == "__main__":
    main()
