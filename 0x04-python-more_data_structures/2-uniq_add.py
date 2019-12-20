#!/usr/bin/python3

my_list = [1, 2, 3, 1, 4, 2, 5]
def uniq_add(my_list=[]):
    sum = 0
    unique = list(set(my_list))
    for i in unique:
        sum += i
    return sum
