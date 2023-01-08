#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])
    
    except (ZeroDivisionError, TypeError, IndexError) as ex:
        result = None
        print("Exception: {}".format(ex), file=sys.stderr)

    return (result)
