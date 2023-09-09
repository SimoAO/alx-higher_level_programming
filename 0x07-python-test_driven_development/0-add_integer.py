#!/usr/bin/python3
"""This module defines the sum of 2 integers.
"""


def add_integer(a, b=98):
    """
    A function that adds 2 integers.
    Args:
    a: first integer
    b: second integer
    Returns:
    the sum
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
