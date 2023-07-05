#!/usr/bin/python3

"""
A funtion that adds 2 integer numbers together
and return the sum of the two numbers
"""


def add_integer(a, b=98):
    """
    Calculate sum of two numbers
    Args:
        a (int): First integer
        b (int): second integer (optional)

    Returns:
        Sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
