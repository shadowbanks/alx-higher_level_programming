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
        if not isinstance(value, int) or type(value) == bool:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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

class Square(BaseGeometry):
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
