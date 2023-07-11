#!/usr/bin/python3
"""The save_to_json_file module"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file,
    using a JSON representation
    """
    with open(fielname, "w", encoding="utf-8") as fn:
        json.dump(my_obj, fn)
