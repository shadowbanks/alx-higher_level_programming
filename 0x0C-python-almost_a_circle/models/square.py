#!/usr/bin/python3
"""
Module ```Square``` creates a square inheriting from a super class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Create a square based of the ``rectangle`` super class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
