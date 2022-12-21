#!/usr/bin/python3
"""
Task 6-scuare.py
This is a Class Square with private instance attrib
"""


class Square:
    """
    Class Square with private instance attrib size
    and Public instance method: area(self)
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.
        Args:
            size (int): Size of square.
            position (int, int): position of square.
        """
        self.__size = size
        self.position = position
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if (len(self.__position) != 2 or not isinstance(self.__position, tuple) or
                not all(isinstance(i, int) for i in self.__position) or
                not all(i >= 0 for i in self.__position)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return

        for h in range(0, self.__position[1]):
            print()

        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for k in range(0, self.__size):
                print("#", end="")
            print()
