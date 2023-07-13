#!/usr/bin/python3
"""
Module ```100-my_int``` doc
"""


class MyInt(int):
    """ Make a custom int class"""
    def __eq__(self, value):
        return int.__ne__(self, value)

    def __ne__(self, value):
        return int.__eq__(self, value)
