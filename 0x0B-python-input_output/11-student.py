#!/usr/bin/python3
"""the student module"""


class Student:
     """a class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """initialize a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for j in attrs:
                if j in self.__dict__:
                    dic[j] = self.__dict__[j]
            return dic

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            self.__dict__[key] = value
