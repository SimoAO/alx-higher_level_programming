#!/usr/bin/python3
"""The Student class"""


class Student:
    """A class named Stuednt
    """

    def __init__(self, first_name, last_name, age):
        """Initializes an instance of variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation of the student"""
        return self.__dict__
