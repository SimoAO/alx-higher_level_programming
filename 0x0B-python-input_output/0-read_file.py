#!/usr/bin/python3
"""The read_file module"""


def read_file(filename=""):
    """a function that reads a text file (UTF8)
    and prints it to stdout
    """
    with open(filename, "r", encoding="utf-8") as fn:
        tx = fn.read()
        print(tx, end="")
