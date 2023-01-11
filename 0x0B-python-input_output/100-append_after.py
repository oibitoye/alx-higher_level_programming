#!/usr/bin/python3
"""
filename: 100-append_after.py
function that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file,
    after each line containing a specific string
    """

    with open(filename, "r", encoding="utf-8") as file:
        tlines = file.readlines()

    with open(filename, "w", encoding="utf-8") as file2:
        new_str = ""
        for line in tlines:
            new_str += line
            if search_string in line:
                new_str += new_string
        file2.write(new_str)
