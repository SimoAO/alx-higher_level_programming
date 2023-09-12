#!/usr/bin/python3
"""The load_from_json_file module"""
import json


def load_from_json_file(filename):
    """a function that creates an Object from a “JSON file”"""
    with open(filename, encoding="utf-8") as fn:
        return json.load(fn)
