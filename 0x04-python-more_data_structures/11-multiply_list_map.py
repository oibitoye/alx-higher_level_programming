#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = my_list.copy()
    for i in range(0, len(my_list)):
        new_list[i] = my_list[i] * number
