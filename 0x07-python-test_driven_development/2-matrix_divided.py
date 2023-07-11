#!/usr/bin/python3

"""
A function that divides every element
of a matrix by a number
"""


def matrix_divided(matrix, div):
    """
    Divide all element of a matrix by "div"
    Args:
        matrix (list): A list of lists of integers/floats
        div (int, float): A number to divide the matrix

    Return:
        A new matrix of the results
    """
    if (not len(matrix) > 0 or
            not all(isinstance(x, list) and len(x) > 0 for x in matrix)) or \
            (not isinstance(matrix, list)):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    if not all(isinstance(x, (int, float)) for rows in matrix for x in rows):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    if not all(len(x) == len(matrix[0]) for x in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(y/div, 2) for y in x] for x in matrix]
