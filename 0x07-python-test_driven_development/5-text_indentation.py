#!/usr/bin/python3
"""
This module defines the text_indentation function
"""


def text_indentation(text):
    """
    Function that prints indented text.
    """

    if type(text) != str:
        raise TypeError("text must be a string")
    i = 0
    g = ""
    for j in text:
        if i == 1:
            g = ""
            i = 0
        if j not in "?:.":
            g += j
        else:
            g += j
            print(g.strip())
            print()
            i = 1
    if i == 0 and '\n' not in g:
        print(g.strip(), end="")
    elif i == 0:
        print(g.strip())
