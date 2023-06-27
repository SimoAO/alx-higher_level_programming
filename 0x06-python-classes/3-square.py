#!/usr/bin/python3
"""the square module"""


class Square:
    """defines the square"""
    def __init(self, size=0):
        """
        Args:
        size: length of the side
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

        def area(self):
            """Calculates the area of the square
            Returns: the area of the square
            """
            return slef.__size * self.__size
