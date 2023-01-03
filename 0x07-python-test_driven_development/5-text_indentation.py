#!/usr/bin/python3
"""
Task 5-text_indentation.py
This is a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Function to print Texts
    """

    if isinstance(text, str):
        xter = [".", "?", ":"]
        note = False
        for letter in text:
            if note:
                if letter == " ":
                    continue
                else:
                    note = True
            else:
                if letter in xter:
                    print(letter + "\n")
                    note = False
                else:
                    print(letter,end="")
    else:
        raise TypeError("text must be a string")
