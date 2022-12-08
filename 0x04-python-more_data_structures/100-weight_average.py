#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None:
        if len(my_list):
            numb = 0
            density = 0
            for i in my_list:
                numb = numb + (i[0] * i[1])
                density = density + i[1]
            weight = (numb / density)
            return weight
    return 0
