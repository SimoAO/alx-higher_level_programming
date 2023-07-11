#!/usr/bin/python3
"""The pascal_triangle module"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal’s triangle of n"""
    if n <= 0:
        return []
    tr = []
    ro = []
    for x in range(n):
        ro = [1]
        if x > 0:
            for y in range(x):
                ro.append(sum(tr[-1][y:y+2]))
        tr.append(ro)
    return tr
