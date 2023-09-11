#!/usr/bin/python3
"""The MyInt module"""


class MyInt(int):
    """A class named MyInt"""

    def __eq__(self, value):
        """Swaps the == with !="""
        return self.real != value

    def __ne__(self, value):
        """Swaps the != with == """
        return self.real == value
