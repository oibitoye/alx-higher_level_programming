#!/usr/bin/python3
"""
filename: 12-pascal_triangle.py
function returns a list of lists of
integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    function returns pascal triangle of n.
    """

    if not n > 0:
        return []

    minm = n - 1
    shape = [[1]]

    for i in range(minm):
        row = []
        row.append(1)

        if len(shape[i]) > 1:
            prev_len = len(shape[i]) - 1
            nextl = 1

            for j in range(prev_len):
                tot = shape[i][j] + shape[i][nextl]
                row.append(tot)
                nextl += 1

        row.append(1)
        shape.append(row)

    return shape
