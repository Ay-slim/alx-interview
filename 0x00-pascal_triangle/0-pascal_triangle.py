#!/usr/bin/python3
"""
Pascal's triangle module
"""


def pascal_triangle(n):
    """
    A function that returns pascal's triangle for an integer
    @n: Integer argument
    Return: A list with the pascal's triangle values
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    pas_tri = [1, 1]
    full_ret_list = [[1], [1, 1]]
    if n == 2:
        return full_ret_list
    int_arg_counter = 3
    while int_arg_counter <= n:
        new_vals = [1, 1]
        for i in range(len(pas_tri) - 1):
            new_vals.insert(i+1, pas_tri[i] + pas_tri[i+1])
        pas_tri = new_vals
        full_ret_list.append(pas_tri)
        int_arg_counter += 1
    return full_ret_list
