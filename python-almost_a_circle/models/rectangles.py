#!/usr/bin/python3
"""Rectangle that inherits from Base"""
from models.base import Base

class Rectangle(Base):
        """Rectangle Class"""

        def __init__(self, width, height, x=0, y=0, id=None):
               """initialize rectangle object"""
                super().__init__(id)
                self.width = width
                self.height = height
                self.x = x
                self.y = y

        def __str__(self):
            """ String representation of Rectangle """
            rep = "[Rectangle] ({}) {}/{}".format(self.id, self.x, self.y)
            rep += " - {}/{}".format(self.width, self.height)
            return rep

        def to_dictionary(self):
            """ Dictionary representation of Rectangle """
            return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}

        def display(self):
            """ Visual representation of Rectangle """
            print("\n" * self.y, end='')
            for row in range(self.height):
            print(" " * self.x + "#" * self.width)

        def area(self):
            """ Area of Rectangle """
            return self.width * self.height

        def update(self, *args, **kwargs):
            """ Update values of Rectangle """
            my_list = list(args)
            attr = ["id", "width", "height", "x", "y"]

        if args:
            for i in range(len(my_list)):
                setattr(self, attr[i], my_list[i])

        else:
            for k, v in kwargs.items():
                setattr(self, k, v)
                

        @property
        def width(self):
             return self.__width
        
        @property
        def height(self):
             return self.__height
        
        @property
        def x(self):
             return self.__x
        
        property
        def y(self):
             return self.__y
        
        @width.setter
        def width(self, width):
             self.int_validator(width, "width")
             self.__width = width

        @height.setter
        def height(self, width):
             self.int_validator(height, "height")
             self.__height = height

        @x.setter
        def x(self, x):
             self.int_validator(x, "x")
             self.__x = x


        @y.setter
        def y(self, y):
             self.int_validator(y, "y")
             self.__y = y
        