#!/usr/bin/python3
"""the square module"""

class Square:
    """defines a square"""

    def __init__(self, size=0):
        """
        args:
        size: length of a side
        """
        self.__size = size

    @property
    def size(self):
        """
        the size of the side
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """calculates the area of the square
        returns: the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """prints the square with the character #"""
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
