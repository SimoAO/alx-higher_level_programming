#!/usr/bin/python3
"""The rectangle module"""


class Rectangle:
    """Defines a rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Args:
        height: height of the ractangle
        width: width of the rectangle
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def height(self):
        """The height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """The width of the rectangle"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """Returns the rectangle with # character"""
        if self.__height == 0 or self.__width == 0:
            return ("")
        return (("#" * self.__width + "\n") * self.__height)[:-1]

    def __repr__(self):
        """Returns a rperesentation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Prints the message after deleting a rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
