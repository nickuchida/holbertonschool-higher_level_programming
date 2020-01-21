#!/usr/bin/python3
'''
7 integer validator
'''


class BaseGeometry:
    def area(self):
        '''public instance area'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''public instance method for validating value'''
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
