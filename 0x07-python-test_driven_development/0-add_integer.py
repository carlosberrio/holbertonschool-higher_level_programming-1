#!/usr/bin/python3
"""Module for add_integer method"""


def add_integer(a, b=98):
    """Adds 2 integers
    Args:
        int a: first arg num
        int b: second arg num, default value = 98
    Returns:
        integer: the addition of a and b
    Raises:
        TypeError: if a or b are not integers or floats
    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
