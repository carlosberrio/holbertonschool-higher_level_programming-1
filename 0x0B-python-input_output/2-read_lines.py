#!/usr/bin/python3
"""Module for read_lines method"""


def read_lines(filename="", nb_lines=0):
    """Reads n lines of a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as file:
        if nb_lines <= 0:
            print(file.read(), end="")
            return
        for n, line in enumerate(file):
            if n == nb_lines:
                break
            print(line, end="")
