#!/usr/bin/python3
'''
0-rectangle
'''


class Rectangle:
    '''
    class Rectangle
    '''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        'getter'
        return self.__width
    @width.setter
    def width(self, value):
        'setter'
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')

    @property
    def height(self):
        '''getter'''
        return self.__height
    @height.setter
    def height(self, value):
        '''setter'''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
