#!/usr/bin/python3
"""
Module ```base``` contains the base class of the project
"""


class Base:
    """ Base class of the shapes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializing the class"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @classmethod
    def value_check(cls, name, value, mode):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0 and mode == 1:
            raise ValueError(f"{name} must be > 0")
        elif value <= 0 and mode == 2:
            raise ValueError(f"{name} must be >= 0")
