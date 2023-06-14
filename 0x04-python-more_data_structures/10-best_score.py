#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        max_score = max(i for i in a_dictionary.values())
        return "".join([x for x, y in a_dictionary.items() if y == max_score])
    else:
        return None
