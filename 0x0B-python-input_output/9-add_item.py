#!/usr/bin/python3
"""
Module for add_item method
Adds all arguments to a Python list, and then save them to a file
"""
import sys
import os.path
"""The os module provides methods for file processing"""

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
jsonlist = []

if os.path.exists(filename):
    jsonlist = load_from_json_file(filename)

for arg in sys.argv[1:]:
    jsonlist.append(arg)

save_to_json_file(jsonlist, filename)
