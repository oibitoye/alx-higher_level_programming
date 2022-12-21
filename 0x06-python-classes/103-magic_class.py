#!/usr/bin/python3
"""Python class MagicClass that does exactly as the bytecode provided"""

import math


class MagicClass:
    """MagicClass Class"""

    def __init__(self, radius=0):
        """Init a MagicClass.
        Arg:
            radius (float or int): radius
        """
        self.__radius = 0
        if type(radius) is not float and type(radius) is not int:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def circumference(self):
        return 2 * math.pi * self.__radius
