#!/usr/bin/python3

"""
This function prints out a person's name
"""
import doctest


def say_my_name(first_name, last_name=""):
    """
    Prints out full name, the last name is optional
    Args:
        first_name (str): User's first name
        last_name (str): User's last name (optional)
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    doctest.testfile("./tests/3-say_my_name.txt")
