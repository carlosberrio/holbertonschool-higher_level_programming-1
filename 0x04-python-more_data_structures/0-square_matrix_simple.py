#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
        return [list(map((lambda n: n**2), submat)) for submat in matrix]
"""
def square_matrix_simple(matrix=[]):
        new_matrix = []
        for submat in matrix:
                new_matrix += [list(map((lambda n: n**2), submat))]
        return new_matrix
"""
