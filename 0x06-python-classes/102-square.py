#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initializes a square - Constructor
        Args:
            size (int): length of a side of the square
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the square's area

        Returns:
            Current square area
        """
        return self.__size ** 2

    def __ne__(self, other):
        """Compare if square is not equal to another based on area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size != other.size

    def __eq__(self, other):
        """Compare if square is equal to another based on area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size == other.size

    def __gt__(self, other):
        """Compare if square is greater than another based on area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size > other.size

    def __lt__(self, other):
        """Compare if square is less than another based on area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size < other.size

    def __ge__(self, other):
        """Compare if square is greater than or equal to another based on area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size >= other.size

    def __le__(self, other):
        """Compare if square is less than or equal to another based on area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size <= other.size
