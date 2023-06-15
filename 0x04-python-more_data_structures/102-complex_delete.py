#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        del_keys = [x for x, y in a_dictionary.items() if y == value]
        for x in del_keys:
            del a_dictionary[x]
    return a_dictionary
