#!/usr/bin/python3
def no_c(my_string):
    """Remove all character c/C from a string"""

    new_str = ""
    for x in my_string:
        if x != "c" and x != "C":
            new_str += x
    return new_str
