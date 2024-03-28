#!/usr/bin/python3
"""rotae 2d matrix"""


def rotate_2d_matrix(matrix):
    """the function"""
    # transpose
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse the matrix
    for i in range(len(matrix)):
        matrix[i].reverse()
