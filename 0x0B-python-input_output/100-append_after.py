#!/usr/bin/python3
"""the append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """a function that inserts a line of text to a file,
    after each line containing a specific string
    """
    ms = ""
    with open(filename, "r", encoding="utf_8") as fn:
        for ln in fn:
            ms += ln
            if search_string in ln:
                ms += new_string

    with open(filename, "w", encoding="utf_8") as fn:
        fn.write(ms)
