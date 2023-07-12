#!/usr/bin/python3
"""
Module ```11-student``` documentation
"""


class Student:
    """ Create a student class"""
    def __init__(self, first_name, last_name, age):
        """ Instantaion of Class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Convert attributes to dictionary"""
        if isinstance(attrs, list):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__

    def reload_from_json(self, json):
        """ Reload a dictionary"""
        for x in json.keys():
            setattr(self, x, json[x])
