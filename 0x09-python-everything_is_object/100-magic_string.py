#!/usr/bin/python3
def magic_string():
    magic_string.c = getattr(magic_string, "n", 0) + 1
    return ("BestSchool, " * (magic_string.c - 1) + "BestSchool")
