#!/usr/bin/python3
"""The lookup module"""


def lookup(obj):
    """A function that returns the list of available
    attributes and methods of an object
    Args:
    obj: the object looking for
    Returns:
    a list object
    """
    return dir(obj)
