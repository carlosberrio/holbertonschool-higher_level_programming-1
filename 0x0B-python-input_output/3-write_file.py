#!/usr/bin/python3
"""Module for write_file method"""


def write_file(filename="", text=""):
    """writes a string <text> to a text file (UTF8) <filename>
    and returns the number of characters written"""
    with open(filename, 'w', encoding='utf-8') as file:
        """f.write(string) writes the contents of string to the file,
        returning the number of characters written"""
        return file.write(text)
