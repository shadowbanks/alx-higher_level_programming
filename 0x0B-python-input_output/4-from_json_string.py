#!/usr/bin/python3
"""
Module ```4-from_json_string``` documentation
"""
import json


def from_json_string(my_str):
    """ Convert a JSON representation to a object"""
    return json.loads(my_str)
