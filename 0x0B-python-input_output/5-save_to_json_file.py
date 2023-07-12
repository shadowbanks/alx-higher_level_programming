#!/usr/bin/python3
"""
Module ```5-save_to_json_file``` documentation
"""
import json


def save_to_json_file(my_obj, filename):
    """ Write an object to a text file"""
    with open(filename, "w", encoding="utf-8") as fd:
        fd.write(json.dumps(my_obj))
