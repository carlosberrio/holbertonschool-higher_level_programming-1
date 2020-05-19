#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initializes a square
        Args:
            size (int): length of a side of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
