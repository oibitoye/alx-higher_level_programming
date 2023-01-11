#!/usr/bin/python3
"""
filename: 1-write_file.py
function that writes a string to a text file (UTF8)
and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8)
    """

    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
