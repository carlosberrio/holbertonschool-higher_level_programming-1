#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square - Constructor
        Args:
            size (int): length of a side of the square
            position (int, int): coordinates of the square
        """
        self.__size = size
        self.__position = position

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
        else:
            self.__position = value

    @property
    def position(self):
        """Property for coordinates of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Raises:
            TypeError: if tuple does not have two integers
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Calculates the square's area

        Returns:
            Current square area
        """
        return self.__size ** 2

    def my_print(self):
        """Prints square or new line if size is 0 """
        if self.__size is 0:
            print()
            return

        for s in range(self.__position[1]):
            print()

        for r in range(self.__size):
            print("".join([' ' for s in range(self.__position[0])]), end="")
            print("".join(['#' for c in range(self.__size)]))
