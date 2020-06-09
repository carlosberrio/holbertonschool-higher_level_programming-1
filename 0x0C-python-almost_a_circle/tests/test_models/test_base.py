#!/usr/bin/python3
"""Unittest for Base Class Module"""
import unittest
from json import dumps, loads
from os import path
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """Test Cases for Base Class Module Functionality"""
    # ------------- Tests for Constructor --------------
    def test_nb_instances_private(self):
        """Tests if nb_objects is a private instance"""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_class_instantiation(self):
        """Tests different 'valid' Base() instantiations"""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        b4 = Base()
        b5 = Base(None)
        self.assertEqual(str(type(b1)), "<class 'models.base.Base'>")
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b1.id, b3.id - 1)
        self.assertEqual(b1.id, b4.id - 2)
        self.assertEqual(b1.id, b5.id - 3)
        self.assertEqual(b1.__dict__, {"id": 1})

    def test_class_unusual_instantiation(self):
        """Tests different 'invalid' Base() instantiations"""
        self.assertEqual("Hakuna", Base("Hakuna").id)
        self.assertEqual(5.5, Base(5.5).id)
        self.assertEqual([2, 3], Base([2, 3]).id)
        self.assertEqual({'1': 2}, Base({'1': 2}).id)
        self.assertEqual(True, Base(True).id)

    def test_sync_arguments(self):
        """Tests id after sequence"""
        b = Base()
        b = Base(None)
        b = Base(98)
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_id_from_variable(self):
        """Test id passed from variable"""
        bid = 100
        b = Base(bid)
        self.assertEqual(b.id, bid)

    def test_exceptions(self):
        """Test for min/max arguments"""
        with self.assertRaises(TypeError):
            Base.__init__()
        with self.assertRaises(TypeError):
            Base(10, 10)  # b = Base(10, 10)

# Tests for to_JSON

# Tests from_JSON

# Save to file

# Create

# Load from file

if __name__ == '__main__':
    unittest.main()
