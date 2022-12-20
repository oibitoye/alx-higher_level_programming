#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    pos = 0
    for i in my_list:
        try:
            print("{:d}".format(my_list[i]), end='')
        except (ValueError, TypeError):
            pass
        else:
            pos = pos + 1
    print("")
    return pos
