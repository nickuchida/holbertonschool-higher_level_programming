#!/usr/bin/python3
'''
module base
'''
import json


class Base:
    '''base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''initalizes base'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        '''return json string representation'''
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    def from_json_string(json_string):
        '''return list of json string representation'''
        if json_string is None:
            return []
        return json.loads(json_string)
