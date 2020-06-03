#!/usr/bin/python3
"""Module for MyInt class"""


class MyInt(int):
    def __eq__(self, other):
        """inverts equal"""
        return int(self) != int(other)

    def __ne__(self, other):
        """inverts non-equal"""
        return int(self) == int(other)
