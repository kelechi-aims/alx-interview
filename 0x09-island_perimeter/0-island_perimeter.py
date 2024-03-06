#!/usr/bin/python3
'''
Island Perimeter
'''


def island_perimeter(grid):
    '''
    A function  that returns the perimeter of the island described in grid
    '''
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Start with assuming all sides are exposed

                # Check neighboring cells
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Deduct 2 if adjacent cell is also land
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Deduct 2 if adjacent cell is also land

    return perimeter
