#!/usr/bin/python3
def multiple_returns(sentence):
    if (len(sentence) == 0):
        tuple_new = (len(sentence), None)
    else:
        tuple_new = (len(sentence), sentence[0])
    return (tuple_new)
