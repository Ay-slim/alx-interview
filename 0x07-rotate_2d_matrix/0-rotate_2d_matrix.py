#!/usr/bin/python3
"""Module for rotating an nxn matrix in place"""


from typing import List


def reverse_list(list_arg: List) -> None:
    """Reverses a list"""
    half = len(list_arg) // 2
    start = 0
    end = len(list_arg) - 1
    for l in range(half):
        tmp = list_arg[start + l]
        list_arg[start + l] = list_arg[end - l]
        list_arg[end - l] = tmp

def rotate_2d_matrix(matrix: List) -> None:
    """Function to rotate a 2d matrix"""
    n = len(matrix)
    for i in range(n - 1):
        for j in range(i + 1, n):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp
    for each_row in matrix:
        reverse_list(each_row)
