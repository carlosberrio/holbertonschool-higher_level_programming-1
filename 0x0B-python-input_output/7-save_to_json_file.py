#!/usr/bin/python3
"""Module for from_json_string method"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object <my_obj> to a text file <filename>,
    using a JSON representation"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
