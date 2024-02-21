#!/usr/bin/python3
"""Module for rotating an nxn matrix in place"""


def rotate_2d_matrix(matrix: list) -> None:
    """Function to rotate a 2d matrix"""
    n = len(matrix)
    for i in range(n - 1):
        for j in range(i + 1, n):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp
    for each_row in matrix:
        half = len(each_row) // 2
        start = 0
        end = len(each_row) - 1
        for step in range(half):
            tmp = each_row[start + step]
            each_row[start + step] = each_row[end - step]
            each_row[end - step] = tmp
