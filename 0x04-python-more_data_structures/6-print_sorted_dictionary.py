#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dic = list(a_dictionary.keys())
    for key in new_dic.sort():
        print(key, ":", a_dictionary[key])
