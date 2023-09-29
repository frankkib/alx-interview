#!/usr/bin/python3
"""
The perimeter module
"""


def island_perimeter(grid):
    """
    Function that returns perimeter of the
    of the island described
    """
    if grid is None:
        return 0
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 1
                if row < rows - 1 and grid[row + 1][col] == 1:
                    perimeter -= 1
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 1
                if col < cols - 1 and grid[row][col + 1] == 1:
                    perimeter -= 1
    return perimeter
