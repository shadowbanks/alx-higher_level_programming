#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # print(matrix)
    for i in matrix:
        # print(i)
        for j in i:
            # print(j)
            print("{:d}".format(j), end=" " if j != i[len(i) - 1] else "")
        print()
