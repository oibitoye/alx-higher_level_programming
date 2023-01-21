#!/usr/bin/python3
"""This Module contains class Square,
an inheritance of the class Rectangle
"""
from models.rectangle import Rectangle as Rect


class Square(Rect):
    """ Inherit Class Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes Square instances """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str special method """
        return (
            f"[Square] ({self.id}) {self.x}/{self.y} "
            f"- {self.width}/{self.height}"
        )

    @property
    def size(self):
        """ Getter size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter size """
        self.width = value
        self.height = value

    def __str__(self):
        """ str special method """
        return (
            f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
        )

    def update(self, *args, **kwargs):
        """ update method """
        if args is not None and len(args) > 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a dictionary with attributes """
        list_atr = ['id', 'size', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            if key == 'size':
                dict_res[key] = getattr(self, 'width')
            else:
                dict_res[key] = getattr(self, key)

        return dict_res
