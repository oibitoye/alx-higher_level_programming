#!/usr/bin/python3
def max_integer(my_list=[]):
    len_list = len(my_list)

    if len_list == 0:
        return (None)
    max_num = -30000000
    for i in range(1, length):
        if max_num < my_list[i]:
            max_num = my_list[i]

    return (max_num)
