#!/usr/bin/python3
"""The Base class"""


import json


class Base:
    """A class named Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initiliazes an instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
