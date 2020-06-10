#!/usr/bin/python3
"""Unittest for Rectangle Class Module"""
import unittest
import io
from contextlib import redirect_stdout
from random import randrange
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """
    Test Cases for Rectangle Class Module Functionality
    """
    def setUp(self):
        """Reset instances for all tests"""
        Base._Base__nb_objects = 0

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
            r = Rectangle()
        err_msg = "__init__() missing 2 required \
positional arguments: 'width' and 'height'"
        self.assertEqual(str(error.exception), err_msg)

        with self.assertRaises(TypeError) as error:
            r = Rectangle(1)
        err_msg = "__init__() missing 1 required \
positional argument: 'height'"
        self.assertEqual(str(error.exception), err_msg)

        with self.assertRaises(TypeError) as error:
            r = Rectangle(10, 2, 10, 10, 10, 5)
        err_msg = "__init__() takes from 3 to 6 \
positional arguments but 7 were given"
        self.assertEqual(str(error.exception), err_msg)

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
                    float('-inf'), 6j, [1], {100}, float('nan'), None]

        r = Rectangle(1, 2)
        attributes = ["width", "height", "x", "y"]
        for attribute in attributes:
            s = '{} must be an integer'.format(attribute)
            for invalid_type in invtypes:
                # print(s, invalid_type)
                with self.assertRaisesRegex(TypeError, s):
                    setattr(r, attribute, invalid_type)

    # TESTS VALUE EXCEPTIONS FOR WIDTH, X & Y
    def test_invalid_type_value_for_the_checker(self):
        """Test to validate width, height, x, and y type values"""
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertRaises(TypeError, Rectangle, "1", 2)
        self.assertRaises(TypeError, Rectangle, 1, "2")
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")

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

    # ------------- Tests for Methods --------------
    def test_area(self):
        """Test area method"""
        r = Rectangle(5, 5)
        self.assertEqual(r.area(), 25)
        r = Rectangle(10, 2, 5)
        self.assertEqual(r.area(), 20)
        r = Rectangle(4, 15, 1, 4, 99)
        self.assertEqual(r.area(), 60)

    def test_area_args(self):
        """Test too many args for area"""
        r = Rectangle(8, 1)
        with self.assertRaises(TypeError):
            r.area(10)

    def test_str(self):
        """Test for the __str__ method"""
        r = Rectangle(8, 12, 2, 1, 12)
        self.assertEqual(r.__str__(), "[Rectangle] (12) 2/1 - 8/12")
        r = Rectangle(5, 5, 1, 1)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 1/1 - 5/5")
        r = Rectangle(22, 22, 0)
        self.assertEqual(r.__str__(), "[Rectangle] (2) 0/0 - 22/22")
        r = Rectangle(33, 33)
        self.assertEqual(r.__str__(), "[Rectangle] (3) 0/0 - 33/33")

    def test_basic_display(self):
        """Test display without x and y"""
        r = Rectangle(5, 5)
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 5 + "\n") * 5)
        r = Rectangle(5, 3, 0, 0, 1)
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 5 + "\n") * 3)

    def test_display_with_coordinates(self):
        """Test display with x and y"""
        r = Rectangle(10, 2, 5)
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
            self.assertEqual(output, (" " * 5 + "#" * 10 + "\n") * 2)
        r = Rectangle(4, 15, 1, 4, 99)
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
            self.assertEqual(
                output, (("\n" * 4) + (" " * 1 + "#" * 4 + "\n") * 15))
        r = Rectangle(5, 3, 0, 0, 1)
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
            self.assertEqual(output, (" " * 0 + "#" * 5 + "\n") * 3)

    def test_update(self):
        """ Tests Method update with pack args """
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(25, 5, 10, 89, 90)
        self.assertEqual(r.__str__(), "[Rectangle] (25) 89/90 - 5/10")

    def test_to_dict(self):
        """Test regular to_dictionary"""
        r = Rectangle(10, 2, 5)
        d = r.to_dictionary()
        d1 = {"id": 1, "width": 10, "height": 2, "x": 5, "y": 0}
        self.assertEqual(d1, d)
        self.assertTrue(type(d1) is dict)

        r = Rectangle(4, 15, 1, 4, 99)
        d = r.to_dictionary()
        d2 = {'id': 99, 'width': 4, 'height': 15, 'x': 1, 'y': 4}
        self.assertEqual(d2, d)
        self.assertTrue(type(d2) is dict)

        r = Rectangle(5, 3, 0, 0, 1)
        d = r.to_dictionary()
        d3 = {'id': 1, 'width': 5, 'height': 3, 'x': 0, 'y': 0}
        self.assertEqual(d3, d)
        self.assertTrue(type(d3) is dict)

        r_up = Rectangle(1, 1, 1, 1, 1)
        r_up.update(**d3)
        self.assertEqual(str(r), str(r_up))
        self.assertNotEqual(r, r_up)
