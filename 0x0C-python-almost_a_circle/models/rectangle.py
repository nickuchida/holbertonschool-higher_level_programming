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
        print(rectangle[:-1])

    def __str__(self):
        '''print string representation of rectangle'''
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        '''update rectangle'''
        if len(args) > 0:
            if len(args) == 0:
                return
            elif len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.width = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
            elif len(args) == 5:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
        if len(kwargs) > 0:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        '''returns dictionary representation of rectangle'''
        dicrep = {}
        dicrep['id'] = self.id
        dicrep['width'] = self.width
        dicrep['height'] = self.height
        dicrep['x'] = self.x
        dicrep['y'] = self.y
        return dicrep
