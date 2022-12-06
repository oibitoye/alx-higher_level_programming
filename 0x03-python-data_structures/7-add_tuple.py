#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a == 0:
        a_one = 0
        a_two = 0
    elif len_a == 1:
        a_one = tuple_a[0]
        a_two = 0
    else:
        a_one = tuple_a[0]
        a_two = tuple_a[1]

    if len_b == 0:
        b1 = 0
        b2 = 0
    elif len_b == 1:
        b1 = tuple_b[0]
        b2 = 0
    else:
        b1 = tuple_b[0]
        b2 = tuple_b[1]

    tuple_new = (a_one + b1, a_two + b2)

    return (tuple_new)
