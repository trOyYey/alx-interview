#!/usr/bin/python3
'''
island_perimeter mod
'''


def island_perimeter(grid):
    '''
    returns the perimeter of the island described in grid
    '''
    perimeter = 0
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 1 if i == 0 else not grid[i - 1][j]
                perimeter += 1 if i == rows - 1 else not grid[i + 1][j]
                perimeter += 1 if j == 0 else not grid[i][j - 1]
                perimeter += 1 if j == cols - 1 else not grid[i][j + 1]
    return perimeter
