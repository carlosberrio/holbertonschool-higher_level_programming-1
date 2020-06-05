#!/usr/bin/python3
"""Module for append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line
    containing a specific string"""
    with open(filename, 'r+', encoding='utf-8') as file:
        new_text = ""
        for line in file:
            new_text += line
            if search_string in line:
                new_text += new_string
        file.seek(0)
        file.write(new_text)
