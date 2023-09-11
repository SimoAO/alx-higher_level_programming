#!/usr/bin/python3
"""The add_attribute module"""


def add_attribute(objec, attribute, value):
    """Add a new attribute if not already assigned
    """
    if not hasattr(objec, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(objec, attribute, value)
