#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i, j in enumerate(my_list):
        new_list = my_list
        if j == search:
            new_list[i] = replace
    return new_list
