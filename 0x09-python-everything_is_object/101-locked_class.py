#!/usr/bin/python3
"""The locked class module"""


class LockedClass:
    """
    Prevents the user from creating new instance attributes
    except if the new instance attribute is called first_name
    """

    __slots__ = "first_name"
