#!/usr/bin/python3
"""
Class that defines a Rectangle based on 0-rectangles
"""


class Rectangle:
    """
    Class defines rectangle
    """

    def __init__(self, width=0, height=0):
        """ Method that initializes the instance
        Args:
            width: width of rectangle
            height: height rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ returns width
        Returns:
            width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """ defines the width
        Args:
            value: width
        Raises:
            TypeError if width is not an integer
            ValueError if width is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

    @property
    def height(self):
        """ returns height
        Returns:
            height of the rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """ defines the height
        Args:
            value: height
        Raises:
            TypeError if height is not an integer
            ValueError if height is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
