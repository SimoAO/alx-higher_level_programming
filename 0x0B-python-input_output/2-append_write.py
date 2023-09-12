#!/usr/bin/python3
"""The append_write module"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file
    Args:
    filename: the file name
    Returns:
    the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as fn:
        return fn.write(text)
