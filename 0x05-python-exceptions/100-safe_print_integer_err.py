#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    status = True
    try:
        print("{:d}".format(value))

    except (ValueError, TypeError) as ex:
        status = False
        print(ex, file=sys.stderr)

    return (status)
