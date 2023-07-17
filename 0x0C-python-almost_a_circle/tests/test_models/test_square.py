#!/usr/bin/python3
"""
Unittest for ```Square``` class
"""
import unittest
import json
from io import StringIO
from unittest.mock import patch
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Test the class ``Square`` and
    ensure everything works as it should
    """

    def setUp(self):
        Square._Base__nb_objects = 0

    def test_class_doc(self):
        """ Test if the Square class has a docstring."""
        self.assertIsNotNone(Square.__doc__)

    def test_method_doc(self):
        """ Test if the methods in Square class has a docstring."""
        methods = [
                Square.__init__,
                Square.update,
                Square.to_dictionary,
                Square.__str__
                ]
        for method in methods:
            self.assertIsNotNone(method.__doc__)

    def test_constructor(self):
        """ Test the constructor with valid ids"""
        r1 = Square(10, 0, 0, 12)
        r2 = Square(14)
        r3 = Square(10, 1, 1)

        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 12)

        self.assertEqual(r2.width, 14)
        self.assertEqual(r2.height, 14)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 1)

        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 10)
        self.assertEqual(r3.x, 1)
        self.assertEqual(r3.y, 1)
        self.assertEqual(r3.id, 2)

        self.assertRaises((TypeError), Square, "name", 2)
        self.assertRaises((TypeError), Square, 2, "3")
        self.assertRaises((ValueError), Square, -2)
        self.assertRaises((ValueError), Square, 2, -3, 1)
        self.assertRaises((TypeError), Square, 2, "x")
        # self.assertRaises((ValueError), Square, 2, 3, 3, -1)
        self.assertRaises((TypeError), Square, 2, 3, 3, "1")

    def test_area(self):
        """ Test the area method"""
        r = Square(2)
        r1 = Square(3, 1, 1, 13)
        self.assertEqual(r.area(), 4)
        self.assertEqual(r1.area(), 9)

    def test_display(self):
        """ Test the display method"""
        r1 = Square(4)
        expected_output = "####\n####\n####\n####\n"

        r2 = Square(2, 2, 2)
        expected_output2 = "\n\n  ##\n  ##\n"

        r3 = Square(3, 1, 0)
        expected_output3 = " ###\n ###\n ###\n"

        with patch("sys.stdout", new=StringIO()) as redirect_stdout:
            r1.display()
            self.assertEqual(redirect_stdout.getvalue(), expected_output)

        with patch("sys.stdout", new=StringIO()) as redirect_stdout2:
            r2.display()
            self.assertEqual(redirect_stdout2.getvalue(), expected_output2)

        with patch("sys.stdout", new=StringIO()) as redirect_stdout3:
            r3.display()
            self.assertEqual(redirect_stdout3.getvalue(), expected_output3)

    def test_update_args(self):
        """ Test only args of update method
        prototype def(self, *args, **kwargs)
        args input order:
            id, width, height, x, y
        kwargs takes key:value pair of the attributes
        """
        r1 = Square(10, 10, 10)

        r1.update(89)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.id, 89)

        r1.update(89, 2)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.id, 89)

        r1.update(89, 2, 3)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.id, 89)

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 89)

    def test_update_kwargs(self):
        """ Test kwargs of update method
        prototype def(self, *args, **kwargs)
        args input order:
            id, width, height, x, y
        kwargs takes key:value pair of the attributes
        """
        r1 = Square(10, 10, 10)

        r1.update(size=1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.id, 1)

        r1.update(size=1, x=2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.id, 1)

        r1.update(y=3, id=89, size=2, x=3)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.id, 89)

    def test_str(self):
        """ Test the __str__ method"""
        r = Square(10, 1, 2, 3)
        expected_str = "[Square] (3) 1/2 - 10"
        self.assertEqual(str(r), expected_str)


if __name__ == "__main__":
    unittest.main()
