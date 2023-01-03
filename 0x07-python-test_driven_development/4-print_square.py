#!/usr/bin/python3
"""
Task 4-print_square.py
This is a function that prints a square with the character #
"""


def print_square(size):
    """
    Function to print a square with the character #
    """
    if isinstance(size, int) or not (isinstance(size, float) and size < 0):
        if size >= 0:
            print(("#" * size + "\n") * size, end="")
        else:
            raise ValueError("size must be >= 0")
    else:
        raise TypeError("size must be an integer")
