#!/usr/bin/python3
""" The append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """A function that inserts a line of text to a file, after
        each line containing a specific string
    """
    mt = ""
    with open(filename, encoding="utf8") as fn:
        for line in fn:
            mt += line
            if search_string in line:
                mt += new_string

    with open(filename, mode="w") as fn:
        fn.write(mt)
