#!/usr/bin/python3
"""
Module ```0-read_file``` documentation
"""


def read_file(filename=""):
    """ Read a file"""
    with open(filename, encoding="utf-8") as fd:
        print(fd.read())
