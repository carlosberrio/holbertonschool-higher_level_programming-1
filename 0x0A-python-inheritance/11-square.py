#!/usr/bin/python3
"""
Module for Square subclass,
contains BaseGeometry Class and subclass Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a Square subclass"""
    def __init__(self, size):
        """Square Instantiation - Constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method - Calculates area"""
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
