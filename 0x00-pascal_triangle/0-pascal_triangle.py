#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Initialize the row with 1's
        row = [1] * (i + 1)
        # Update the elements in the middle of the row
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        # Append the completed row to the triangle
        triangle.append(row)

    return triangle
