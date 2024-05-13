#!/usr/bin/python3
"""Write a class Square that defines a squre"""


class Square:
    """private instance attribute: __size"""

    def __init__(self, size=0):
        self.__size = size
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
