#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        pos = 0
        for i in my_list:
            if x > pos:
                print("{}".format(i), end="")
                pos = pos + 1
        print("")
    except SyntaxError:
        print("Syntax Error Occured")
