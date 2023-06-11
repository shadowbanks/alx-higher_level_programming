#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print the reverse of a list integer"""

    for x in reversed(my_list):
        print("{:d}".format(x))
