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

    def to_json(self):
        return self.__dict__
