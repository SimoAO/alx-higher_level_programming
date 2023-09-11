#!/usr/bin/python3
"""This module defines a class named MyList"""


class MyList(list):
    """A class MyList that inherits from list"""
    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))
