#!/usr/bin/python3
"""The Rectangle module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """a way to calculate the area"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the representation of the recttangle"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
