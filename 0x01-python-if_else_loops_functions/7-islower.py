#!/usr/bin/python3

def islower(c):
    """Check if a character is lowercase"""

    if (ord(c) < 97 or ord(c) > 122):
        return (False)
    return (True)
