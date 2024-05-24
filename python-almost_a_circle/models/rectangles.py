#!/usr/bin/python3
"""rectangle that inherits from Base"""
from models.base import Base

class Rectangle(Base):

        def __init__(self, width, height, x=0, y=0, id=None):
                self.__width = width
                self.__height =  height
                self.__x = x
                self.__y = y
                self.id = id

        @property