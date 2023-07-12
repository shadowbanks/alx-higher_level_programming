#!/usr/bin/python3
"""
Module ```2-append_write``` documentation
"""


def append_write(filename="", text=""):
    """  Append a file"""
    with open(filename, "a", encoding="utf-8") as fd:
        f_write = fd.write(text)
    return f_write
