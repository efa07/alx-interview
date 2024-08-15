#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """
    Rotates the given n x n 2D matrix 90 degrees clockwise in-place.
    """
 # First, we reverse the order of the rows
    matrix.reverse()
    
    # Next, we swap the elements in the diagonal only once
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]