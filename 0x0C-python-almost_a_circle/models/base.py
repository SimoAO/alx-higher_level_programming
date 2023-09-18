#!/usr/bin/python3
"""The Base class"""


import json


class Base:
    """A class named Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initiliazes an instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        list_dicts = []
        fn = cls.__name__ + ".json"
        if list_objs is None:
            with open(fn, "w",  encoding='utf-8') as f:
                f.write(Base.to_json_string(list_dicts))
            return
        for i in list_objs:
            list_dicts.append(i.to_dictionary())
        with open(fn, "w",  encoding='utf-8') as f:
            f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ is "Rectangle":
            ob = cls(2, 5)

        if cls.__name__ is "Square":
            ob = cls(2)
        ob.update(**dictionary)
        return ob

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        fn = cls.__name__ + ".json"
        list_dicts = []
        if path.exists(fn) is False:
            return []
        with open(fn, "r",  encoding='utf-8') as f:
            list_dicts = Base.from_json_string(f.read())
            for value, key in enumerate(list_dicts):
                list_dicts[key] = cls.create(**list_dicts[key])
            return list_dicts
