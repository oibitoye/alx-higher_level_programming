#!/usr/bin/python3
"""
filename: 11-student.py
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

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.
        """
        for attr in json:
            self.__dict__.update({attr: json[attr]})
