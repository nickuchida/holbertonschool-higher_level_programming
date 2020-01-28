#!/usr/bin/python3
'''
module rectangle
'''
from models.base import Base


class Rectangle(Base):
    '''class rectangle inherits from base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter'''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''getter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''setter'''
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''setter'''
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''returns area value of rectangle'''
        return self.__width * self.__height

    def display(self):
        '''print rectangle using #s'''
        rectangle = ''
        for i in range(self.__y):
            rectangle += '\n'
        for y in range(self.__height):
            for x in range(self.__x):
                rectangle += ' '
            rectangle += '#' * self.__width + '\n'
        print(rectangle)

    def __str__(self):
        '''print string representation of rectangle'''
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)
