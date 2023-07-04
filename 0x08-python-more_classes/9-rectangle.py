#!/usr/bin/python3
"""
A class definition of a rectangle
"""


class Rectangle:
    """This is a class that defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiate the class"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        a = Rectangle.area(rect_1)
        b = Rectangle.area(rect_2)
        if a >= b:
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    def area(self):
        """ Calculate the area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculate the perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """Output string of the rectangle drawing"""
        return "\n".join(
                [type(self).print_symbol * self.__width
                    for _ in range(self.__height)])

    def __repr__(self):
        """Return string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.height})"

    def __del__(self):
        """Print a goodbye message when an instance get's deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
