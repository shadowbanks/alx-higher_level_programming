#!/usr/bin/python3
"""
Module ```base``` contains the base class of the project
"""
import json


class Base:
    """ Base class of the shapes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializing the class"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @classmethod
    def value_check(cls, name, value, mode):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0 and mode == 1:
            raise ValueError(f"{name} must be > 0")
        elif value <= 0 and mode == 2:
            raise ValueError(f"{name} must be >= 0")

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Convert a dictionary to a JSON"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save a JSON into a file"""
        name = cls.__name__ + ".json"
        output = []
        if list_objs is not None:
            for i in list_objs:
                output.append(i.to_dictionary())
        save = Base.to_json_string(output)
        with open(name, "w", encoding="utf-8") as fd:
            fd.write(save)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of JSON string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if dictionary is not None and len(dictionary) != 0:
            if cls.__name__ == "Rectangle":
                cls_dummy = cls(1, 1)
            elif cls.__name__ == "Square":
                cls_dummy = cls(1)
            cls_dummy.update(**dictionary)
        return cls_dummy
