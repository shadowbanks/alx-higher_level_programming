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

    def update(self, *args, **kwargs):
        if len(args) > 0:
            assign = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                if assign[i] == "size":
                    size_t = ["width", "height"]
                    for j in range(len(size_t)):
                        setattr(self, size_t[j], value)
                else:
                    setattr(self, assign[i], value)
        elif kwargs is not None:
            for i, value in kwargs.items():
                if i == "size":
                    size_t = ["width", "height"]
                    for j in range(len(size_t)):
                        setattr(self, size_t[j], value)
                else:
                    setattr(self, i, value)

    def to_dictionary(self):
        """ Return a dictionary representation of the square"""
        return {"id":self.id, "size":self.width,
                "x":self.x, "y":self.y}
    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
