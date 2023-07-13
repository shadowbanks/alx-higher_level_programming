#!/usr/bin/python3
"""
Module ```101-add_attribute``` doc
"""


def add_attribute(a_class, name, value):
    """ Set a new attribute if the attribute
    does not already exist
    """
    if not hasattr(a_class, name):
        setattr(a_class, name, value)
    else:
        raise TypeError("can't add new attribute")
