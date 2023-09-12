#!/usr/bin/python3
"""The paascal_triangle module"""


def pascal_triangle(n):
    """eturns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    pl = []
    r = []
    for i in range(n):
        r = [1]
        if i > 0:
            for j in range(i):
                r.append(sum(pl[-1][j:j+2]))
        pl.append(r)
    return pl
