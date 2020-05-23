#!/usr/bin/python3
""" Module for matrix_divided method"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div
    Args:
        matrix: list of lists of numbers (int or float)
        div: int or float to divide matrix by
    Returns:
        list: a new matrix list of lists
    Raises:
        TypeError: if div is not an int or float
        ZeroDivisionError: if div is equal to 0
        TypeError: if matrix or each row is not a list of lists
                   of int or floats
        TypeError: if each row of the matrix is not of the same size
        TypeError: if any element of the sublist is not an int or float
    """
    if type(div) not in (int, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError('matrix must be a matrix (list of lists) ' +
                        'of integers/floats')

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError('matrix must be a matrix (list of lists) ' +
                            'of integers/floats')
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')

        for n in row:
            if type(n) not in (int, float):
                raise TypeError('matrix must be a matrix (list of lists) ' +
                                'of integers/floats')

    return [[round(n / div, 2) for n in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
