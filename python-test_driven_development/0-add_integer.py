#!/usr/bin/python3
"""
adds 2 integers; 2 input numbers a and/or b could be float types,
but must be first casted to integers; b has initialed value, 98.
"""


def add_integer(a, b=98):
    """a function adds 2 integers"""

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
