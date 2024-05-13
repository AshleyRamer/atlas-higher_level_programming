#!/usr/bin/python3
"""Write a class Square that defines a squre"""


class Square:
    """private instance attribute: __size"""

    @property
    def size(self):
        """retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter"""
        self.__position = value

    def __init__(self, size=0, position=(0, 0)):
        """initialize"""
        self.__size = size
        if isinstance(position, tuple) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) < 2 or isinstance(position[1], int) is False:
            raise IndexError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """gets area"""
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        elif self.__position is None:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print("{}".format(" ") * self.__position[0], end="")
                print("{}".format("#") * self.__size, end="")
                print()
