#!/usr/bin/python3
"""Island perimeter"""

def island_perimeter(grid):
    """
    island_perimeter - Function to calculate the perimeter of an island
    @grid: List of list of numbers
    Returns: Number representing island perimeter
    """
    rowLen = len(grid)
    if (rowLen > 0):
        colLen = len(grid[0])
    perimeter = 0
    for row in range(rowLen):
        for col in range(colLen):
            if grid[row][col] == 1:
                if row == 0 or grid[row+1][col] == 0:
                    perimeter += 1
                if col == 0 or grid[row][col+1] == 0:
                    perimeter += 1
                if row == rowLen - 1 or grid[row - 1][col] == 0:
                    perimeter += 1
                if col == colLen - 1 or grid[row][col - 1] == 0:
                    perimeter += 1
    return perimeter