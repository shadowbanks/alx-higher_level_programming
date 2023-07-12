#!/usr/bin/python3
"""
Module ```8-class_to_json``` documentation
"""
import json


def class_to_json(obj):
    """ Convert a class to a json
    A dictionary descriptionn with simple data structure
    """
    return (json.dumps(obj.__dict__))
