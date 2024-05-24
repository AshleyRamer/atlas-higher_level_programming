#!/usr/bin/python3
"""defines base class"""

class Base:
    """private class variable"""
    __nb_objects =0 

    def __init__(self, id=None):
        """initializes object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
