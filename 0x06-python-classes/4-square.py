#!/usr/bin/python3
"""
Task 4-scuare.py
This is a Class Square with private instance attrib
"""


class Square:
    """
    Class Square with private instance attrib size
    and Public instance method: area(self)
    """
    def __init__(self, size=0):
        self.__size = size
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
