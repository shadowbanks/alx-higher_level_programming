#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Print an integer safely"""
    try:
        print("{:d}".format(value))
    except ValueError as er:
        print(f"Exception: {er}", file=sys.stderr)
        return False
    return True
