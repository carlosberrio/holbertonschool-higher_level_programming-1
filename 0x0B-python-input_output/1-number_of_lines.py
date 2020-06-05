#!/usr/bin/python3
"""Module for number_of_lines method"""


def number_of_lines(filename=""):
    """Returns the number of lines of a text file"""
    with open(filename, encoding="utf-8") as file:
        """readlines() Returns a list of lines from the file"""
        return len(file.readlines())
