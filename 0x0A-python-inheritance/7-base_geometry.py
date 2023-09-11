#!/usr/bin/python3
"""The BaseGeometry module"""


class BaseGeometry:
    """a class BaseGeometry"""
    def area(self):
        """a way to calculate the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a method to validate value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
