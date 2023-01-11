#!/usr/bin/python3
"""
filename: 10-student.py
A class Student that defines a student
"""


class Student:
    """
    A class Student that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """init the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary definition"""
        st_dict = {}
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            for item in attrs:
                if item in self.__dict__:
                    st_dict.update({item: self.__dict__[item]})
            return st_dict
        return self.__dict__.copy()
