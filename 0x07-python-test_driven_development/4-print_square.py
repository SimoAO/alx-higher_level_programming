#!/usr/bin/python3
"""
This module defines the print_square function
"""


def print_square(size):
    """
    Function that prints a square with # charcter.
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        for i in range(0, size):
            for j in range(0, size):
                print("#", end="")
            print()
