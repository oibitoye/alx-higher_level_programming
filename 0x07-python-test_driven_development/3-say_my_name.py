#!/usr/bin/python3
"""
Task 3-say_my_name.py
This is a function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Function to Prints "My name is" followed by the
    first name and optional last name
    """
    if not(isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    elif not(isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    else:
        print("My name is", first_name, last_name)
