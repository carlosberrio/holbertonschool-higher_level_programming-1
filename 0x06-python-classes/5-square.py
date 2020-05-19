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
        """Property for length of a side of the square"""
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

    def my_print(self):
        """Prints square or new line if size is 0 """
        for r in range(self.__size):
            for c in range(self.__size):
                print('#', end="\n" if c is self.size - 1 and r != c else "")
        print()
