#!/usr/bin/python3
"""
This function prints a sqaure
"""
import doctest


def print_square(size):
    """
    Print a square based of the size passed to it
    Args:
        size: size of each side of the square
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and int(size) < 0:
        raise TypeError("size must be an integer")
    size = int(size)
    for i in range(size):
        print("#" * size)


if __name__ == "__main__":
    doctest.testfile("./tests/4-print_square.txt")
