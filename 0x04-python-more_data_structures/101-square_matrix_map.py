#!/usr/bin/python3
def square_matrix_map(matrix=[]) -> list:
    return [list(map(lambda x: x**2, i)) for i in matrix]
