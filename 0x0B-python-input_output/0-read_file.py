#!/usr/bin/python3
'''
module 0-read_file
'''


def read_file(filename=""):
    '''reads text file (UTF8) and prints to stdout'''
    with open(filename, encoding='utf-8') as f:
        for i in f:
            print(i, end='')
