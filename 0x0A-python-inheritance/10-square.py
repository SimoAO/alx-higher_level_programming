#!/usr/bin/python3
"""The Square module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class named Square"""
    def __init__(self, size):
        """Initializes a square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
