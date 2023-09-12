#!/usr/bin/python3
"""The write_file module"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file (UTF8)
    Args:
    filename: the file name
    Returns:
    the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as fn:
        return fn.write(text)
