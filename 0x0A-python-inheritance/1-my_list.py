#!/usr/bin/python3
"""Module for MyList class"""


class MyList(list):
    """Defines MyList class"""
    def print_sorted(self):
        """Method for printing sorted list using Class list"""
        print(sorted(self))
