#!/usr/bin/python3
"""
filename: 5-save_to_json_file.py
function that writes an Object to a
text file, using a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a
    text file, using a JSON representation:
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
