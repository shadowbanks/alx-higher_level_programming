#!/usr/bin/python3
"""
Unittest for ```Base``` class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test the class ``Base`` and ensure everything works as it should"""

    def setUp(self):
        """ Setup to run before every test"""
        Base._Base__nb_objects = 0

    def test_class_doc(self):
        """ Test if the Base class has a docstring."""
        self.assertIsNotNone(Base.__doc__)

    def test_method_doc(self):
        """ Test if the methods in Base class has a docstring."""
        methods = [
                Base.__init__, Base.value_check,
                Base.to_json_string, Base.save_to_file,
                Base.from_json_string, Base.create,
                Base.load_from_file
                ]
        for method in methods:
            self.assertIsNotNone(method.__doc__)

    def test_without_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_with_id(self):
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

    def test_multiple_ids(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_value_check(self):
        with self.assertRaises(TypeError):
            Base.value_check("name", "value", 1)

        with self.assertRaises(ValueError):
            Base.value_check("name", -2, 1)

        with self.assertRaises(ValueError):
            Base.value_check("name", 0, 1)

        with self.assertRaises(ValueError):
            Base.value_check("name", 0, 2)

        self.assertRaises((TypeError), Base.value_check, "width", "string", 1)


if __name__ == "__main__":
    unittest.main()
