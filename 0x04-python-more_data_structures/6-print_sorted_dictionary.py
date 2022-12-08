#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dic = list(a_dictionary.keys())
    new_dic.sort()
    for key in new_dic:
        print("{}: {}".format(key, a_dictionary[key]))
