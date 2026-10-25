#!/usr/bin/python3
"""Island perimeter module."""


def island_perimeter(grid):
    """Return the perimeter of the island described in grid.

    grid is a rectangular list of lists where 0 is water and 1 is land.
    Each land cell adds 4 sides, minus 2 for every land neighbour it
    shares a side with (counted once, looking up and left).
    """
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] != 1:
                continue
            perimeter += 4
            if row > 0 and grid[row - 1][col] == 1:
                perimeter -= 2
            if col > 0 and grid[row][col - 1] == 1:
                perimeter -= 2
    return perimeter
