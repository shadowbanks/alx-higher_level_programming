#!/usr/bin/python3
"""
Module ```base``` contains the base class of the project
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Convert a dictionary to a JSON"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
