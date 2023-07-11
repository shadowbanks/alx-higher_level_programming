#!/usr/bin/python3
"""
Module doc for ```2-is_same_class```
"""


def is_same_class(obj, a_class):
    """
    Compare if two objects are of the same type
    """
    if type(obj) == a_class:
        return True
    return False
