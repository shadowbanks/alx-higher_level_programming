#!/usr/bin/python3
"""
Module doc for ```5-base_geometry```
"""


class BaseGeometry:
    """
    An empty class
    """
    def area(self):
        """ Calcualte the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validate value passed"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
