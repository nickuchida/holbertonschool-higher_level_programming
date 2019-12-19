#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = []
    for i in matrix:
        new = list(map(lambda x: x ** 2, i))
        newmatrix.append(new)
    return newmatrix
