#!/usr/bin/python3
"""Module for LockedClass Class"""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.
    """
    __slots__ = ['first_name']
