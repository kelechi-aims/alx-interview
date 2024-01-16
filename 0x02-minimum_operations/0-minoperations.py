#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """
    Calculate the fewest number of operations to have exactly n 'H'
    characters in the file.

    Args:
    - n (int): The desired number of 'H' characters.

    Returns:
    - int: The fewest number of operations needed.
    """
    if n <= 1:
        return 0  # If n is 1 or less, no operations needed

    operations = 0
    current_H = 1  # Initial 'H' in the file
    clipboard = 1  # Initial content in the clipboard that's been copied

    while current_H < n:
        if n % current_H == 0:
            # If the current number of 'H' is a divisor of n
            clipboard = current_H
            operations += 1
        current_H += clipboard
        operations += 1

    return operations
