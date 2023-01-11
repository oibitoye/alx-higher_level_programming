#!/usr/bin/python3

"""
filename: 0-read_file.py
function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """function that reads a text file (UTF8) """
    with open(filename, encoding='UTF-8') as file:
        for line in file:
            print(line, end='')
