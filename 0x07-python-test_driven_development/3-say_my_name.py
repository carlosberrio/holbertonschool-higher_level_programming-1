#!/usr/bin/python3
"""Module for say_my_name method"""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>
    Args:
        (str) first_name: first string
        (str) last_name: second string, default str = empty
    Raises:
        TypeError: if arguments are not string type
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
