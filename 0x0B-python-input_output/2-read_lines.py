#!/usr/bin/python3
'''
module 2-read_lines.py
'''


def read_lines(filename="", nb_lines=0):
    '''reads n lines of a text file (UTF8) and prints to stdout'''
    count = 0
    with open(filename, encoding='UTF-8') as txtfile:
        for line in txtfile:
            if count < nb_lines and nb_lines != 0:
                print(line, end='')
                count += 1
            elif count == 0:
                print(line, end='')
