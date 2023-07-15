#!/usr/bin/python3
"""
Module ```rectangle``` defines a rectangle
"""
from models.base import Base


class Rectangle(Base):
    """ Create a rectangle with it's properties"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initiziling rectangle"""
        if id is not None:
            super().value_check("id", id, 0)
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        super().value_check("width", width, 1)
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        super().value_check("height", height, 1)
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x != 0:
            super().value_check("x", x, 2)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if y != 0:
            super().value_check("y", y, 2)
        self.__y = y
