#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer([..])"""

    def test_empty_list(self):
        """Tests for empty list"""
        self.assertIsNone(max_integer([]))

    def test_no_args(self):
        """Tests for missing arguments"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Tests for one element"""
        self.assertEqual(max_integer([1]), 1)

    def test_identical(self):
        """Unittest for identical arguments"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_max_start(self):
        """Unittest for max int at start"""
        self.assertEqual(max_integer([1024, 512, 256, 128, 64]), 1024)

    def test_max_end(self):
        """Unittest for max int at end"""
        self.assertEqual(max_integer([32, 64, 128, 256, 512, 1024]), 1024)

    def test_ordered(self):
        """Unittest for an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7, 8]), 8)

    def test_unordered(self):
        """Unittest for an ordered list"""
        self.assertEqual(max_integer([15, -15, -8, 8, 3, -3]), 15)

    def test_negative_num(self):
        """Unittest for negative numbers"""
        self.assertEqual(max_integer([-1, -500, -250, -180]), -1)

    def test_nan(self):
        """Unittest for 'nan'"""
        self.assertEqual(max_integer([999, 0, 1024, float('nan')]), 1024)

    def test_ints_floats(self):
        """Unittest for ints/floats"""
        self.assertEqual(max_integer([-8, 2.5, 100, -45.55, 125, 9.5]), 125)

    def test_inf(self):
        """Unittest for infinity"""
        self.assertEqual(
            max_integer([float('inf'), 1024, float('-inf')]), float('inf'))

    def test_numeric_str(self):
        """Unittest for numeric string"""
        self.assertEqual(max_integer("0123456789"), "9")

    def test_strings(self):
        """Unittest for strings"""
        self.assertEqual(max_integer(["tik", "tak", "tok", "tuk"]), "tuk")

    def test_dif_types(self):
        """Unittest for number lists"""
        self.assertEqual(max_integer([[2], [3], [4, 5], [10], [-5]]), [10])

    def test_characters(self):
        self.assertEqual(
            max_integer(['k', 'o', 'q', 'v', 'n', 'f', 'b', 'z', 'a']), 'z')

    def test_string(self):
        """Unittest for a string"""
        self.assertEqual(max_integer("IthinkIdonotlikeTTD"), "t")

    def test_int(self):
        """Unittest for TypeError"""
        with self.assertRaises(TypeError):
            max_integer(1024)

    def test_dict(self):
        """Unittest for invalid arguments"""
        with self.assertRaises(TypeError):
            max_integer([{1: 2, 3: 4}, {"a": "b", "c": "d"}])

    def test_mixed_list(self):
        """Unittest for mixed list"""
        with self.assertRaises(TypeError):
            max_integer([[514], [0], [-4], "iceCream", [-8, 9], 199])

    def test_none(self):
        """Unittest for None as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == '__main__':
    unittest.main()
