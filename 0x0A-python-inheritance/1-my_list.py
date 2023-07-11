#!/usr/bin/python3
"""
Module doc: Inherit from class list
"""


class MyList(list):
    """
    A class that inherits from the list class
    """
    def print_sorted(self):
        """ Sort the elements and print"""
        my_copy = self[:]
        my_copy.sort()
        print(my_copy)
