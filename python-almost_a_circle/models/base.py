#!/usr/bin/python3
"""defines base class"""

class Base:
    def __init__(self, id=None):
        if id is not None:
            self.id = id
            __nb_objects += 1
        else:
            __nb_objects += 1
            self.id - __nb_objects
