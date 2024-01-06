#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    Args:
    - n (int): The number of rows to generate. Should be a positive integer.

    Returns:
    - list of lists: A list of lists representing Pascal's Triangle
    up to the nth row.
    """
    # check for valid input
    if n <= 0:
        return []

    # Initialize with the first row of Pascal's Triangle
    triangle = [[1]]

    # Generate each row from the second to the nth
    for i in range(1, n):
        # Initialize the new row with the first element as 1
        row = [1]

        # Calculate each element in the row based on the previous row
        for j in range(1, len(triangle[-1])):
            row.append(triangle[-1][j - 1] + triangle[-1][j])

        # Set the last element in the row to 1 and append
        # the row to the triangle
        row.append(1)
        triangle.append(row)

    # Return the complete Pascal's Triangle
    return triangle
