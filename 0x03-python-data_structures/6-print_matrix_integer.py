#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for slist in matrix:
        print(" ".join("{:d}".format(i) for i in slist))
