#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return []
    else:
        sqr_matrix = matrix.copy()
        for i in range(len(matrix)):
            sqr_matrix[i] = list(map(lambda x: x**2, matrix[i]))
        return sqr_matrix
