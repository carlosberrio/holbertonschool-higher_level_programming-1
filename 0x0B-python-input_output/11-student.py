#!/usr/bin/python3
"""Module for Student Class"""


class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        """Object Instantiation
          Args:
            first_name (string): First name of student
            last_name (string): Last name of student
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return self.__dict__
