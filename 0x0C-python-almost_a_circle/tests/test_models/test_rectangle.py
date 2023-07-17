#!/usr/bin/python3
"""
Unittest for ```Rectangle``` class
"""
import unittest
import json
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Test the class ``Rectangle`` and
    ensure everything works as it should
    """

    def setUp(self):
        Rectangle._Base__nb_objects = 0

    def test_class_doc(self):
        """ Test if the Rectangle class has a docstring."""
        self.assertIsNotNone(Rectangle.__doc__)

    def test_method_doc(self):
        """ Test if the methods in Rectangle class has a docstring."""
        methods = [
                Rectangle.__init__, Rectangle.area,
                Rectangle.display, Rectangle.update,
                Rectangle.to_dictionary,
                Rectangle.__str__
                ]
        for method in methods:
            self.assertIsNotNone(method.__doc__)

    def test_constructor(self):
        """ Test the constructor with valid ids"""
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(10, 2)
        r3 = Rectangle(10, 2, 1, 1)

        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 12)

        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 1)

        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 1)
        self.assertEqual(r3.y, 1)
        self.assertEqual(r3.id, 2)

        self.assertRaises((TypeError), Rectangle, "name", 2)
        self.assertRaises((TypeError), Rectangle, 2, "3")
        self.assertRaises((ValueError), Rectangle, -2, 3)
        self.assertRaises((ValueError), Rectangle, 2, -3)
        self.assertRaises((TypeError), Rectangle, 2, 3, "x", 3)
        # self.assertRaises((ValueError), Rectangle, 2, 3, 3, 3, -1)
        self.assertRaises((TypeError), Rectangle, 2, 3, 3, 3, "1")

    def test_area(self):
        """ Test the area method"""
        r = Rectangle(2, 4)
        r1 = Rectangle(3, 4, 1, 1, 13)
        self.assertEqual(r.area(), 8)
        self.assertEqual(r1.area(), 12)

    def test_display(self):
        """ Test the display method"""
        r1 = Rectangle(4, 3)
        expected_output = "####\n####\n####\n"

        r2 = Rectangle(2, 3, 2, 2)
        expected_output2 = "\n\n  ##\n  ##\n  ##\n"

        r3 = Rectangle(3, 2, 1, 0)
        expected_output3 = " ###\n ###\n"

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
        r1 = Rectangle(10, 10, 10, 10)

        r1.update(89)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.id, 89)

        r1.update(89, 2)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.id, 89)

        r1.update(89, 2, 3)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.id, 89)

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.id, 89)

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 89)

    def test_update_kwargs(self):
        """ Test kwargs of update method
        prototype def(self, *args, **kwargs)
        args input order:
            id, width, height, x, y
        kwargs takes key:value pair of the attributes
        """
        r1 = Rectangle(10, 10, 10, 10)

        r1.update(height=1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.id, 1)

        r1.update(width=1, x=2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.id, 1)

        r1.update(y=3, id=89, width=2, x=3)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.id, 89)

        r1.update(width=2, height=3, x=4)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.id, 89)

    def test_str(self):
        """ Test the __str__ method"""
        r = Rectangle(10, 20, 1, 2, 3)
        expected_str = "[Rectangle] (3) 1/2 - 10/20"
        self.assertEqual(str(r), expected_str)


if __name__ == "__main__":
    unittest.main()
