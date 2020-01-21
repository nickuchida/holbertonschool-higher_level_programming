#!/usr/bin/python3
'''
2
'''

def is_same_class(obj, a_class):
    ''' returns True if object is specified class, false if not '''
    if isinstance(obj, a_class):
        return True
    return False
