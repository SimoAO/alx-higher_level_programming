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
        if type(attrs) is list and all(type(i) == str for i in attrs):
            dic = {}
            for j in attrs:
                if j in self.__dict__:
                    dic[j] = self.__dict__[j]
            return dic
        else:
        return self.__dict__
