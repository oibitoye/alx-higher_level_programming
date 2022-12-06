#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    test_div = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            test_div.append(True)
        else:
            test_div.append(False)

    return (test_div)
