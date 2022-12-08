#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        if len(a_dictionary):
            high_score = 0
            high_key = ""
            for key in a_dictionary:
                if a_dictionary[key] > high_score:
                    high_score = a_dictionary[key]
                    high_key = key
            return high_key
    return None
