#!/usr/bin/python3
def raise_exception_msg(message=""):
    """Raise an exception message"""
    try:
        raise NameError
    except NameError:
        print(f"{message}")
