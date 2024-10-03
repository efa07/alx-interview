# Prime Game

## Description

This project contains a Python script named `0-prime_game.py`. The script is designed to determine the winner of a prime number game played between two players, Maria and Ben.

## Files

- `0-prime_game.py`: Contains the implementation of the prime game logic.

## Usage

To use the script, you can import the `isWinner` function from `0-prime_game.py` and call it with the appropriate parameters.

```python
from 0-prime_game import isWinner

# Example usage
x = 5
nums = [1, 2, 3, 4, 5]
print(isWinner(x, nums))
```

## Function

### `isWinner(x, nums)`

Determines the winner of the prime game.

- **Parameters:**
    - `x` (int): The number of rounds.
    - `nums` (list of int): List of integers representing the numbers for each round.

- **Returns:**
    - `str`: The name of the player who won the most rounds. Returns `None` if there is no winner.

## Author

This project is part of the ALX Interview preparation curriculum.