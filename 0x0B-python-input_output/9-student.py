#!/usr/bin/python3
"""
filename: 9-student.py
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

    def to_json(self):
        """returns a dictionary definition"""
        return self.__dict__
