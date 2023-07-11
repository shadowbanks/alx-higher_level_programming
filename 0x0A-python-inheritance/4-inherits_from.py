#!/usr/bin/python3
"""
Module doc for ```4-inherits_from```
"""


def inherits_from(obj, a_class):
    """
    Check if a ``obj`` is an instance of ``a_class``
    that inherited (directly or indirectly)
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
