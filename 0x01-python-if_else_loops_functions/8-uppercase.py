#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 123:
            new_str = ord(str[i]) - 32
        else:
            new_str = ord(str[i])
        print("{:c}".format(new_str), end="")
    print()
