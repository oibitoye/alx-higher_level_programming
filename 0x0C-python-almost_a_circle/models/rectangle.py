#!/usr/bin/python3
"""Module for Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """
    This Rectangle Class can be used to define a rectangle
    ...
    Required Attributes:
    ----------
    width : int
        the width of the rectangle
    height : int
        height of the rectangle
    x : int
        x coordinate
    y : int
        y coordinate
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize instances"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        super().__init__(self.id)

    @property
    def width(self):
        """This is getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """This is setter for width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if not value > 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """This is getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """This is setter for height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if not value > 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """This is getter for x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """This is setter for x attribute"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if not value > 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """getter for y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if not value > 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """This method returns the area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """ This method displays a rectangle """
        rect = self.y * "\n"
        for unit in range(self.height):
            rect += (" " * self.x)
            rect += ("#" * self.width) + "\n"

        print(rect, end='')

    def __str__(self):
        """str method"""
        str_rect = "[Rectangle]"
        str_id = self.id
        str_x = self.x
        str_y = self.y
        str_width = self.width
        str_height = self.height

        return f"{str_rect} ({str_id}) {str_x}/{str_y} - {str_width}/{str_height}"

    def update(self, *args, **kwargs):
        """ update method """
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ method that returns a dictionary with properties """
        list_atr = ['id', 'width', 'height', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            dict_res[key] = getattr(self, key)

        return dict_res
