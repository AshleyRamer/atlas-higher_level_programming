#!/usr/bin/python3
"""Prints a square made out of #s"""

def print_square(size):
    """size is the size length of the square, must be an integer"""

    e1 = "Size must be an integer"
    e2 = "Size must be >= 0"
    if not isinstance(size, int):
        raise TypeError(e1)
    if size < 0:
        raise TypeError(e2)
    if isinstance(size, float) and size < 0:
        raise TypeError(e1)
    for i in range(size):
        print("{}".format("#") * size)
