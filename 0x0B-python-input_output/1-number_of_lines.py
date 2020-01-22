#!/usr/bin/python3
'''
module 1-number_of_lines.py
'''


def number_of_lines(filename=""):
    '''returns number of ines of a text file'''
    count = 0
    with open(filename, encoding='utf-8') as txtfile:
        for i in txtfile:
            count += 1
    return count
