#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary: dict):
    for i, j in sorted(a_dictionary.items()):
        print(f"{i}: {j}")
