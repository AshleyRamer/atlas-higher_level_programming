#!/usr/bin/python3
"""defines base class"""
import json


class Base:
    """
        Attributes: __nb_objects: Instance counter. 
        Methods: __init__: Initializes from Base instance
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def int_validator(self, value, name):
        """Integer Validator"""

        if type(value) is not int:
            raise TypeError(name + " must be an integer")

        if name == "x" or name == "y":
            if value < 0:
                raise ValueError(name + " must be >= 0")
        else:
            if value <= 0:
                raise ValueError(name + " must be > 0")

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert list of dictionaries to JSON string"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Convert JSON string to list of dictionaries """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes JSON string representation of list_objs to a file """
        my_list = []
        if list_objs is not None and len(list_objs) > 0:
            for obj in list_objs:
                my_list.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(my_list))

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances from JSON file """
        list_of_instances = []
        try:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as f:
                my_str = f.read()
                if len(my_str) > 2:
                    for dirt in cls.from_json_string(my_str):
                        list_of_instances.append(cls.create(**dirt))
        except:
            pass
        return list_of_instances

    @classmethod
    def create(cls, **dictionary):
        """ creates an instance of cls with values set """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        else:
            return
        new.update(**dictionary)
        return new
