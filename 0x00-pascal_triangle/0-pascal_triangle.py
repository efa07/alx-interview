#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n.
    """
    arr = []
    if n <= 0:
        return arr
    arr = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(arr[i - 1]) - 1):
            curr = arr[i - 1]
            temp.append(arr[i - 1][j] + arr[i - 1][j + 1])
        temp.append(1)
        arr.append(temp)
    return arr
