#!/usr/bin/python3
"""Unittest for Square Class Module"""
import unittest
import io
from contextlib import redirect_stdout
from random import randrange
from models.base import Base
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """
    Test Cases for Square Class Module Functionality
    """
    def setUp(self):
        Base._Base__nb_objects = 0

    # ------------- Tests for Constructor --------------
    # TESTS CLASS
    def test_class_instance(self):
        """Tests for type, inheritance"""
        class_name = "<class 'models.square.Square'>"
        self.assertEqual(str(Square), class_name)
        self.assertTrue(issubclass(Square, Base))

    def test_class_args_exceptions(self):
        """Test for positional arguments"""
        with self.assertRaises(TypeError) as error:
            Square()
        err_msg = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(error.exception), err_msg)

        with self.assertRaises(TypeError) as error:
            Square(10, 2, 10, 10, 10)
        err_msg = "__init__() takes from 2 to 5 \
positional arguments but 6 were given"
        self.assertEqual(str(error.exception), err_msg)

    # TESTS CONSTRUCTOR
    def test_instantiation(self):
        """Test instantiation with args"""
        r = Square(10, 2, 0, 12)
        self.assertEqual(str(type(r)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(r, Base))
        d = {'_Rectangle__height': 10, '_Rectangle__width': 10,
             '_Rectangle__x': 2, '_Rectangle__y': 0, 'id': 12}
        self.assertDictEqual(r.__dict__, d)

    def test_instantiation_kwargs(self):
        """Test instantiation with kwargs"""
        r = Square(size=15, id=89, y=0, x=50)
        d = {'_Rectangle__height': 15, '_Rectangle__width': 15,
             '_Rectangle__x': 50, '_Rectangle__y': 0, 'id': 89}
        self.assertEqual(r.__dict__, d)


if __name__ == "__main__":
    unittest.main()