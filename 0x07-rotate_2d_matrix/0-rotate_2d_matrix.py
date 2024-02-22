#!/usr/bin/python3
"""Given an n x n 2D matrix, rotate it 90 degrees clockwise
this solution uses in place without using any extra space in memory """


def rotate_2d_matrix(matrix):
    """Rotate 2D Matrix"""
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
