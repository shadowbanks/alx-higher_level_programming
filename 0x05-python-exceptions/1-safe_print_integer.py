#!/usr/bin/python3

def safe_print_integer(value):
    status = False
    try:
        num = int(value)
    except (ValueError, TypeError):
        status = False
        pass
    else:
        print("{:d}".format(num))
        status = True
    return (status)
