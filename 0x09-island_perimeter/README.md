# Island Perimeter

This project involves calculating the perimeter of an island represented by a grid. The grid is a list of lists of integers where:
- `0` represents water
- `1` represents land

## Task

Write a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`.

### Requirements

- The grid is rectangular, with its width and height not exceeding 100.
- The grid is completely surrounded by water.
- There is exactly one island (or one connected component of land cells) in the grid.
- The island doesn't have "lakes" (water inside that isn't connected to the water around the island).

### Example

```python
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

print(island_perimeter(grid))  # Output: 16
```

### Explanation

The perimeter is the sum of the edges of the land cells that are adjacent to water or the grid boundary.

## Usage

To use the `island_perimeter` function, simply import it and pass a grid as an argument:

```python
from island_perimeter import island_perimeter

grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

print(island_perimeter(grid))
```

## Testing

You can test the function using various grid configurations to ensure it correctly calculates the perimeter.
