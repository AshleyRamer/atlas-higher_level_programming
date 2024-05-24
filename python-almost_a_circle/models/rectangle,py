#!/usr/bin/python3
"""Inherits from class Base"""


from models.base import Base


class Rectangle(Base):
    """
        Attributes:
            - id(int): user-specified. Alternatively
            supplied by inherited instance counter

            - width(int): the width of the rectangle
            - height(int): the height of the rectangle
            - x(int): the horizontal print axis
            - y(int): the vertical print axis
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self):
        """STRING representation of triangle"""
        rep = "[Rectangle] ({}) {}/{}".format(self.id, self.x, self.y)
        rep += " - {}/{}".format(self.width, self.height)
        return rep

    def to_dictionary(self):
        """DICTIONARY Representation of rectangle"""
        return {'id: self.id, 'width': self.width, 'height': self.height, 'x': self.x, 'y': self.y}

    def display(self):
        """VISUAL representation of rectangle"""
        print("\n" * self.y, end='')
        for row in range(self.height):
            print(" " * self.x + "#" * self.width)

    def area(self):
        """AREA of rectangle"""
        return self.width * self.height

    def update(self, *args, **kwargs):
        """UPDATE VALUES of rectangle"""
        my_list = list(args)
        attr = ["id", "width", "height", "x", "y"]

        if args:
            for i in range(len(my_list)):
                setattr(self, attr[i], my_list[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, width):
        if isinstance(width, int) and width > 0:
            self.__width = width
        else:
            raise TypeError("width must be an int > 0")

    @height.setter
    def height(self, height):
        if isinstance(height, int) and height > 0:
            self.__height = height
        else:
            raise TypeError("height must be an int > 0")

    @x.setter
    def x(self, x):
        if isinstance(x, int) and x >= 0:
            self.__x = x
        else:
            raise TypeError("x must be an int >= 0")

    @y.setter
    def y(self, y):
        if isinstance(y, int) and y >= 0:
            self.__y = y
        else:
            raise TypeError("y must be an int >= 0")
