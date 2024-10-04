#!/usr/bin/python3
"""
0-pascal_triangle.py module
"""


def pascal_triangle(n):
    """
    generates pascale trinagle lines by the input given
    """
    if n <= 0:
        return []

    p_array = [[] for i in range(n)]

    for i in range(n):
        if i == 0:
            p_array[i].append(1)
            continue

        for j in range(i + 1):
            up_left = p_array[i - 1][j - 1] if j != 0 else 0
            up_right = p_array[i - 1][j] if j != i else 0
            p_array[i].append(up_left + up_right)

    return p_array
