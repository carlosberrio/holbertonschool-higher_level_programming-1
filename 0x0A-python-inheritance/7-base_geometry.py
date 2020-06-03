#!/usr/bin/python3
"""Module for BaseGeometry Class"""


class BaseGeometry:
    """Defines BaseGeometry class"""
    def area(self):
        """Method - Calculates area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Method - Validates value"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
