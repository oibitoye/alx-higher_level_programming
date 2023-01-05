#!/usr/bin/python3
"""
Class that defines a Rectangle based on 0-rectangles
"""


class Rectangle:
    """
    Class defines rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Method that initializes the instance
        Args:
            width: width of rectangle
            height: height rectangle
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ function calculates the Rectangle area
        Returns:
            area of rectangle
        """

        return self.width * self.height

    def perimeter(self):
        """ function calculates the Rectangle perimeter
        Returns:
            perimeter of rectangle
        """

        if self.width == 0 or self.height == 0:
            return 0

        return (self.width * self.width) + (self.height * self.height)

    def __str__(self):
        """ function returns the Rectangle str
        Returns:
            str of the rectangle
        """

        rect = ""

        if self.width == 0 or self.height == 0:
            return rect

        for i in range(self.height):
            rect = rect + (str(self.print_symbol) * self.width) + "\n"

        return rect[:-1]

    def __repr__(self):
        """ function returns the string represantion of the instance
        Returns:
            string represenation of the object
        """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Method that prints a message when the instance is deleted
        """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ function returns the bigger Rectangle
        Args:
            rect_1: Rectangle 1
            rect_2: Rectangle 2
        Raises:
            TypeError when argument is not an instance of the Rectangle class
        Returns:
            The bigger Rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
