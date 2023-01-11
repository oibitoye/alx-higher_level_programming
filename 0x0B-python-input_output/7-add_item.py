#!/usr/bin/python3
"""
filename: 7-add_item.py
script that adds all arguments to a Python
list, and then save them to a file
"""
import os.path
import sys

save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file

FILE = 'add_item.json'
list = []

if os.path.exists(FILE) and os.path.getsize(FILE) > 0:
    my_list = load_from_json(FILE)

if len(sys.argv) > 1:
    for elem in sys.argv[1:]:
        list.append(elem)

save_to_json(list, FILE)
