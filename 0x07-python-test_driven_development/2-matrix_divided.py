#!/usr/bin/python3
"""
Task 2-matrix_divided.py
This is a function to divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Function to divide all elements of a matrix
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    new_matrix = []
    if not isinstance(matrix, list):
        raise TypeError(err_msg)
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        new_row = []
        if not isinstance(row, list):
            raise TypeError(err_msg)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            new_row.append(round(item / div, 2))
        if len(new_row) == len(row):
            new_matrix.append(new_row)
        else:
            raise TypeError("Each row of the matrix must have the same size")
    return new_matrix
