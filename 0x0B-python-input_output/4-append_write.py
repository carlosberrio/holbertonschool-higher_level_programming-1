#!/usr/bin/python3
"""Module for append_write method"""


def append_write(filename="", text=""):
    """appends a string <text> at the end of a text file (UTF8) <filename>
    and returns the number of characters added:"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
