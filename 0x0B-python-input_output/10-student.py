#!/usr/bin/python3
"""
Module ```9-student``` documentation
"""


class Student:
    """ Create a student class"""
    def __init__(self, first_name, last_name, age):
        """ Instantaion of Class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__
