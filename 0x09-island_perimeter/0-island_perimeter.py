#!/usr/bin/python3


def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented in a grid.

    The grid is a list of lists where 0 represents water and 1 represents land.
    The island is surrounded by water and is formed by connecting adjacent
    lands horizontally or vertically.
    The grid is rectangular, with its width and height not exceeding 100.

    Args:
        grid (List[List[int]]): A 2D list representing the map of the island.

    Returns:
        int: The perimeter of the island.

    Example:
        >>> grid = [
        ...     [0, 1, 0, 0],
        ...     [1, 1, 1, 0],
        ...     [0, 1, 0, 0],
        ...     [1, 1, 0, 0]
        ... ]
        >>> island_perimeter(grid)
        16
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add 4 for the current land cell
                perimeter += 4

                # Check if the land cell has a neighboring land cell above
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2

                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

    return perimeter
