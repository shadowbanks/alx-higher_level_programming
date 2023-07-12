#!/usr/bin/python3
"""
Module ```6-load_from_json_file``` documentation
"""
import json


def load_from_json_file(filename):
    """ Create an object from a json file"""
    with open(filename, encoding="utf=8") as fd:
        return json.loads(fd.read())
