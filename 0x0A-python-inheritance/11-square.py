#!/usr/bin/python3
'''
module 11-square.py
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        '''class square'''
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        '''public instance area'''
        return self.__size ** 2

    def __str__(self):
        '''print square size'''
        return '[Square] {}/{}'.format(self.__size, self.__size)
