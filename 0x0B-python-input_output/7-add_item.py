#!/usr/bin/python3
"""
Module ```7-add_item``` documentation
"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item():
    """ Add all arguments to a list and save in a file"""
    n = len(sys.argv)
    my_list = []

    for i in range(1, n):
        my_list.append(sys.argv[i])

    try:
        load = load_from_json_file("add_item.json")
        save = load + my_list
        save_to_json_file(save, "add_item.json")
    except FileNotFoundError:
        save_to_json_file(my_list, "add_item.json")


def main():
    add_item()


main()
