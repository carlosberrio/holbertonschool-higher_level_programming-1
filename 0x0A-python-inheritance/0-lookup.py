#!/usr/bin/python3
"""Module for lookup method"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object
        Args:
            (obj) obj: object to list attributes
        Returns:
            (list): available attributes
    """
    return dir(obj)
