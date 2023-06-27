#!/usr/bin/python3
"""The square module"""
class Square:
    """Defines a square
    Attributes:
    attr1 (size): size of the square
    """
    def __init__(self, size=0):
        """
        Args:
        size: length of a side
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
