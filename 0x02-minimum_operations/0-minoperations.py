#!/usr/bin/env python3
"""Min operations module"""


def minOperations(n) -> int:
    """
    minOperations - Function to calculate the minimum number
    of copy and paste operations on a given input length
    @n: Int input length
    Returns: Int, minimum number of operations
    """
    factor = 2
    operations = 0

    if n <= 1:
        return operations

    while factor ** 2 <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    if n > 1:
        operations += n

    return operations
