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

    def to_json(self, attrs=None):
        """Retrieves dictionary representation of the student"""
        if attrs is None:
            return self.__dict__
        dictionary = {}
        for i in attrs:
            if i in self.__dict__:
                dictionary[i] = self.__dict__[i]
        return dictionary

