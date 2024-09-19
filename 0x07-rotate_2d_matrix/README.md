# README

## Description
This repository contains the solution for rotating a 2D matrix in-place. The algorithm implemented here allows for rotating a square matrix of any size by 90 degrees clockwise.

## Installation
No installation is required for this project. Simply clone the repository and you're good to go!

## Usage
To use the rotation algorithm, follow these steps:
1. Import the `rotate_2d_matrix` function from the `rotate.py` module.
2. Pass the 2D matrix as an argument to the `rotate_2d_matrix` function.
3. The matrix will be rotated in-place, meaning the original matrix will be modified.

## Examples
Here's an example of how to use the `rotate_2d_matrix` function:

```python
from rotate import rotate_2d_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)

print(matrix)
```

Output:
```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

## Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
