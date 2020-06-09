#!/usr/bin/python3
"""Unittest for Rectangle Class Module"""
import unittest
import io
from contextlib import redirect_stdout
from random import randrange
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Test Cases for Rectangle Class Module Functionality"""
    # ------------- Tests for Constructor --------------
    # TESTS CLASS
    def test_class_instance(self):
        """Tests for type, inheritance"""
        class_name = "<class 'models.rectangle.Rectangle'>"
        self.assertEqual(str(Rectangle), class_name)
        self.assertTrue(issubclass(Rectangle, Base))

    def test_class_args_exceptions(self):
        """Test for positional arguments"""
        with self.assertRaises(TypeError) as error:
            Rectangle()
        err_msg = "__init__() missing 2 required \
positional arguments: 'width' and 'height'"
        self.assertEqual(str(error.exception), err_msg)

        with self.assertRaises(TypeError) as error:
            Rectangle(1)
        err_msg = "__init__() missing 1 required \
positional argument: 'height'"
        self.assertEqual(str(error.exception), err_msg)

        with self.assertRaises(TypeError) as error:
            Rectangle(10, 2, 10, 10, 10, 5)
        err_msg = "__init__() takes from 3 to 6 \
positional arguments but 7 were given"
        self.assertEqual(str(error.exception), err_msg)

    # TESTS ID
    def test_rectangle_id(self):
        """Tests id after sequence"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(20, 10)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r4.id, r1.id + 2)

    # TESTS CONSTRUCTOR
    def test_instantiation(self):
        """Test instantiation with args"""
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(str(type(r)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(r, Base))
        d = {'_Rectangle__width': 10, '_Rectangle__height': 2,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 12}
        self.assertDictEqual(r.__dict__, d)

    def test_instantiation_kwargs(self):
        """Test instantiation with kwargs"""
        r = Rectangle(width=10, height=200, id=89, y=0, x=50)
        d = {'_Rectangle__height': 200, '_Rectangle__width': 10,
             '_Rectangle__x': 50, '_Rectangle__y': 0, 'id': 89}
        self.assertEqual(r.__dict__, d)

    # TESTS TYPE EXCEPTIONS
    def test_invalid_type_value(self):
        """Test to validate width, height, x, and y type values"""
        invtypes = [False, 'Matata', (2,), 3.14, -2.5, float('inf'), {1: 10},
                    float('-inf'), [1], {100}, float('nan'), None]

        r = Rectangle(1, 2)
        attributes = ["width", "height", "x", "y"]
        for attribute in attributes:
            s = '{} must be an integer'.format(attribute)
            for invalid_type in invtypes:
                print(s, invalid_type)
                with self.assertRaisesRegex(TypeError, s):
                    setattr(r, attribute, invalid_type)

    # TESTS VALUE EXCEPTIONS FOR WIDTH, HEIGHT, X & Y
    def test_invalid_value(self):
        """Test to validate zero or negative integers"""
        # Test ints <= 0 for width
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 1)
        # Test ints <= 0 for height
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, 0)
        # Test ints < 0 for x
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 1, -1)
        # Test ints < 0 for y
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(1, 1, 1, -1)

    # TESTS VALID VALUES FOR WIDTH, HEIGHT, X & Y
    def test_valid_values(self):
        """Test to validate getters/setters"""
        r = Rectangle(1, 2)
        attributes = ["width", "height", "x", "y"]
        for attribute in attributes:
            n = randrange(10) + 1
            setattr(r, attribute, n)
            self.assertEqual(getattr(r, attribute), n)

    # TESTS VALID VALUES FOR SETTED X & Y VALUES
    def test_setted_values(self):
        """Test for setted attributes"""
        r = Rectangle(1, 2)
        r.x = 5
        r.y = 10
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 10)

    # TESTS FOR AREA, DISPLAY, STR REPRESENTATION AND DICT RPR
    @classmethod
    def setUpClass(cls):
        """Set instances for area and display tests"""
        Base._Base__nb_objects = 0
        cls.r1 = Rectangle(5, 5)
        cls.r2 = Rectangle(10, 2, 5)
        cls.r3 = Rectangle(4, 15, 1, 4, 99)
        cls.r4 = Rectangle(10, 20, 30, 40)

    def test_area(self):
        """test area calculation"""
        self.assertEqual(self.r1.area(), 25)
        self.assertEqual(self.r2.area(), 20)
        self.assertEqual(self.r3.area(), 60)
        self.assertEqual(self.r4.area(), 200)

    def test_area_args(self):
        """Test too many args for area"""
        with self.assertRaises(TypeError):
            r = self.r1.area(10)

    def test_basic_display(self):
        """Test display without x and y"""
        r = Rectangle(5, 3, 0, 0, 1)
        with io.StringIO() as buf, redirect_stdout(buf):
            self.r1.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 5 + "\n") * 5)
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 5 + "\n") * 3)

    def test_display_with_coordinates(self):
        """Test display with x and y"""
        r = Rectangle(5, 3, 0, 0, 1)
        r.display()
        with io.StringIO() as buf, redirect_stdout(buf):
            self.r2.display()
            output = buf.getvalue()
            self.assertEqual(output, (" " * 5 + "#" * 10 + "\n") * 2)
        with io.StringIO() as buf, redirect_stdout(buf):
            self.r3.display()
            output = buf.getvalue()
            self.assertEqual(output, (("\n" * 4) + (" " * 1 + "#" * 4 + "\n") * 15))
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
            print('hola')
            self.assertEqual(output, (" " * 0 + "#" * 5 + "\n") * 3)

    def test_str(self):
        """Test for the __str__ method"""
        self.assertEqual(str(self.r1), "[Rectangle] (1) 0/0 - 5/5")
        self.assertEqual(str(self.r2), "[Rectangle] (2) 5/0 - 10/2")
        self.assertEqual(str(self.r3), "[Rectangle] (99) 1/4 - 4/15")
        self.assertEqual(str(self.r4), "[Rectangle] (3) 30/40 - 10/20")
