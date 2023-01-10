#!/usr/bin/python3
"""
Filename: 1-my_list.py
class inherits from list
"""

class MyList(list):
    """
    Class inherits from list prints the list,
    but sorted (ascending sort)
    """
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
