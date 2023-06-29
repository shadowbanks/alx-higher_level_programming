#!/usr/bin/python3

"""Create a Square class"""


class Square:
    """Create a Square blueprint"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        s = self.__size

        if s == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for i in range(s):
                print(" " * self.__position[0], end="")
                for j in range(s):
                    print("#", end="")
                print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[0], int):
            raise TypeError("size must be an integer")
        self.__position = value
