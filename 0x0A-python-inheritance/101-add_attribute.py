#!/usr/bin/python3
"""
Module ```101-add_attribute``` doc
"""


def add_attribute(a_class, name, value):
    """ Set a new attribute if the attribute
    does not already exist
    """
    if not hasattr(a_class, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(a_class, name, value)
