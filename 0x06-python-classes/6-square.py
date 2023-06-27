#!/usr/bin/python3
"""the square module"""


class Square:
    """defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        args:
        size: length of a side
        position: the square allocation
        """
        self.__size = size
        self.__position = position

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
                    for j in range(self.__position[0]):
                        print(" ", end="")
                    print()
                for i in range(self.__position[1]):
                    print()
            else:
                print()

        @property
        def position(self):
            """the position of hte square"""
            return self.__position

        @position.setter
        def position(self, value):
            """sets the position of the square"""
            if type != tuple or len(value) != 2:
                raise TypeError("position must be a tuple of 2 positive integers")
            if type(value)  
