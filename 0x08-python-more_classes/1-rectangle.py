#!/usr/bin/python3
"""the rectangle module"""


class Rectangle:
    """defines a rectangle"""

    def __init__(self, width=0, height=0):
        """
        args:
        height: height of the ractangle
        width: width of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """the width of the rectangle"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
