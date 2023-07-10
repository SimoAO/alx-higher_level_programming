#!/usr/bin/python3
"""The mylist class module"""


class MyList(list):
    """a class MyList that inherits from list"""
    def print_sorted(self):
        """Returns: prints the list, but sorted"""
        print(sorted(self))
