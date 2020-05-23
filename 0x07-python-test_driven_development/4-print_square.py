#!/usr/bin/python3
"""Module for print_square method"""


def print_square(size):
    """Prints a square with the character '#'
    Args:
        (int) size:length of the square's side
    Raises:
        TypeError: if size is not a integer
        ValueError: if size is less than 0
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    print(('#' * size + '\n') * size, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
