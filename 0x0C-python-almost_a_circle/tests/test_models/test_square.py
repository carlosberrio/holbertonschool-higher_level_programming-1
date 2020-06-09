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
        """Reset instances for all tests"""
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

    # TESTS ID
    def test_Square_id(self):
        """Tests id after sequence"""
        r1 = Square(10, 2)
        r2 = Square(2, 10)
        r3 = Square(10, 2, 0, 12)
        r4 = Square(20, 10)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r4.id, r1.id + 2)

    # TESTS VALUE EXCEPTIONS FOR WIDTH, X & Y
    def test_invalid_type_value(self):
        """Test to validate size, x, and y type values"""
        s = Square(1, 2)
        self.assertEqual(s.size, 1)
        self.assertRaises(TypeError, Square, 1.2)
        self.assertRaises(TypeError, Square, 2, 3.3, 9)
        self.assertRaises(TypeError, Square, float('inf'))
        self.assertRaises(TypeError, Square, float('nan'))
        self.assertRaises(TypeError, Square, 3, float('inf'), 3)
        self.assertRaises(TypeError, Square, 3, 2, float('nan'))

        self.assertRaises(TypeError, Square, None)
        self.assertRaises(TypeError, Square, 2, None, 0)
        self.assertRaises(TypeError, Square, 1, 9, None)

        self.assertRaises(TypeError, Square, "abc")
        self.assertRaises(TypeError, Square, 1, "abc", 0)
        self.assertRaises(TypeError, Square, 2, 1, "abc")

    # TESTS VALUE EXCEPTIONS FOR WIDTH, X & Y
    def test_invalid_value(self):
        """Test to validate zero or negative integers"""
        # Test ints <= 0 for width
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Square(0)
        # Test ints < 0 for x
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Square(1, -1)
        # Test ints < 0 for y
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Square(1, 1, -1)

    # TESTS VALID VALUES FOR WIDTH, HEIGHT, X & Y
    def test_valid_values(self):
        """Test to validate getters/setters"""
        r = Square(2)
        attributes = ["size", "x", "y"]
        for attribute in attributes:
            n = randrange(10) + 1
            setattr(r, attribute, n)
            self.assertEqual(getattr(r, attribute), n)

    # TESTS VALID VALUES FOR SETTED X & Y VALUES
    def test_setted_values(self):
        """Test for setted attributes"""
        r = Square(1, 2)
        r.x = 5
        r.y = 10
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 10)

    # ------------- Tests for Methods --------------
    def test_area(self):
        """test area method"""
        s = Square(5)
        self.assertEqual(s.area(), 25)
        s = Square(10, 2, 5)
        self.assertEqual(s.area(), 100)
        s = Square(4, 15, 1, 99)
        self.assertEqual(s.area(), 16)

    def test_area_args(self):
        """Test too many args for area"""
        s = Square(8, 1)
        with self.assertRaises(TypeError):
            s.area(10)

    def test_str(self):
        """Test for the __str__ method"""
        s = Square(8, 12, 2, 12)
        self.assertEqual(s.__str__(), "[Square] (12) 12/2 - 8")
        s = Square(5, 5, 1, 1)
        self.assertEqual(s.__str__(), "[Square] (1) 5/1 - 5")
        s = Square(22, 22, 0)
        self.assertEqual(s.__str__(), "[Square] (1) 22/0 - 22")
        s = Square(33, 33)
        self.assertEqual(s.__str__(), "[Square] (2) 33/0 - 33")

    def test_basic_display(self):
        """Test display without x and y"""
        s = Square(1)
        r = Square(5, 0, 0, 1)
        with io.StringIO() as buf, redirect_stdout(buf):
            s.display()
            output = buf.getvalue()
            self.assertEqual(output, "#\n")
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 5 + "\n") * 5)

    def test_display_with_coordinates(self):
        """Test display with x and y"""
        s1 = Square(5, 3, 0, 1)
        s2 = Square(10, 2, 5)
        s3 = Square(4, 15, 1, 99)
        with io.StringIO() as buf, redirect_stdout(buf):
            s2.display()
            output = buf.getvalue()
            self.assertEqual(output, (
                ("\n" * 5) + (" " * 2 + "#" * 10 + "\n") * 10))
        with io.StringIO() as buf, redirect_stdout(buf):
            s3.display()
            output = buf.getvalue()
            self.assertEqual(output, (
                ("\n" * 1) + (" " * 15 + "#" * 4 + "\n") * 4))
        with io.StringIO() as buf, redirect_stdout(buf):
            s1.display()
            output = buf.getvalue()
            self.assertEqual(output, (
                ("\n" * 0) + (" " * 3 + "#" * 5 + "\n") * 5))

    def test_update(self):
        """ Tests Method update with pack args """
        s = Square(1, 1, 1)
        s.update(25, 5, 10, 89)
        self.assertEqual(s.__str__(), "[Square] (25) 10/89 - 5")

    def test_to_dict(self):
        """Test regular to_dictionary"""
        r = Square(10, 2, 5)
        d = r.to_dictionary()
        d1 = {'id': 1, 'size': 10, 'x': 2, 'y': 5}
        self.assertEqual(d1, d)
        self.assertTrue(type(d1) is dict)

        r = Square(4, 15, 1, 99)
        d = r.to_dictionary()
        d2 = {'id': 99, 'size': 4, 'x': 15, 'y': 1}
        self.assertEqual(d2, d)
        self.assertTrue(type(d2) is dict)

        r = Square(5, 3)
        d = r.to_dictionary()
        d3 = {'id': 2, 'size': 5, 'x': 3, 'y': 0}
        self.assertEqual(d3, d)
        self.assertTrue(type(d3) is dict)

        r_up = Square(1, 1, 1, 1)
        r_up.update(**d3)
        self.assertEqual(str(r), str(r_up))
        self.assertNotEqual(r, r_up)


if __name__ == "__main__":
    unittest.main()
