#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        for i in my_list:
            if i == idx:
                new_list.append(element)
            else:
                new_list.append(i)
    return new_list
