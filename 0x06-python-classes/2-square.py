#!/usr/bin/python3
"""
Task 2-scuare.py
This is a Class Square with private instance attrib
"""


class Square:
    """
    Class Square with private instance attrib
    """
    def __init__(self, size=0):
        self.__size = size
        if self.__size is not int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
