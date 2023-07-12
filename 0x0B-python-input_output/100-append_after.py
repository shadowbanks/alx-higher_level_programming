#!/usr/bin/python3
"""
Module ```100-append_after``` documentation
"""


def append_after(filename="", search_string="", new_string=""):
    """Append a line of text to a file, after each specified string"""
    output_str = ""
    with open(filename, encoding="utf-8") as fd:
        for line in fd:
            output_str += line
            if search_string in line:
                output_str += new_string
    with open(filename, "w", encoding="utf-8") as fds:
        fds.write(output_str)
