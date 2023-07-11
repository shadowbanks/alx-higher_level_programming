#!/usr/bin/python3
"""
Module doc for ```9-rectangle```
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle class inherting from BaseGeometry
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """Return string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
