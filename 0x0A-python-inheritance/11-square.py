#!/usr/bin/python3
"""
Module doc for ```5-base_geometry```
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A Square class inherting from BaseGeometry
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        """Return string representation of the rectangle"""
        return f"[Square] {self.__size}/{self.__size}"
