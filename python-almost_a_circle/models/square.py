#!/usr/bin/python3
""" Square module that defines the Square class """
from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class: Inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, x, y, id)

    def __str__(self):
        """STRING representation of Square"""

    def to_dictionary(self):
        """DICTIONARY representation of Square"""

    def update(self, *args, **kwargs):
        """UPDATE value od Square"""

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.int_validator(value, "width")
        self.width = value
        self.height = value