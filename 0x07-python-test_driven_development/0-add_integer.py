#!/usr/bin/python3
"""
Task 0-add_integers.py
This is a function to add integers
"""


def add_integer(a, b=98):
    """
    Function to add two integers
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
