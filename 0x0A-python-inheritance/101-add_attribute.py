#!/usr/bin/python3
""""Module for add_atribute method"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it’s possible
    Args:
        (object) obj
        (string) name: object's attribute
        (string) value: attribute's value
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise Exception("can't add new attribute")
