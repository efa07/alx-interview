# 0x01. Lockboxes
Welcome to the 0x01. Lockboxes project! This directory contains a solution to the lockboxes problem, where you need to determine if all the boxes can be opened given a set of keys.

## Problem Description
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

## Objective
Write a method that determines if all the boxes can be opened.

- Prototype: def canUnlockAll(boxes)
- boxes is a list of lists.
- A key with the same number as a box opens that box.
- You can assume all keys will be positive integers.
- There can be keys that do not have boxes.
- The first box boxes[0] is unlocked.
- Return True if all boxes can be opened, else return False.
## Requirements
* Python 3.x
## Function Implementation
### 'canUnlockAll'
This function checks if all boxes can be opened starting from the first box using a depth-first search (DFS) approach.

### Arguments
* boxes (List[List[int]]): A list of lists where each sublist contains integers representing the keys to other boxes.
### Returns
* bool: True if all boxes can be unlocked, False otherwise.
Example
```python
def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    opened = [False] * n
    opened[0] = True

    def dfs(box):
        for key in boxes[box]:
            if key < n and not opened[key]:
                opened[key] = True
                dfs(key)

    dfs(0)
    return all(opened)

if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Output: True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Output: True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Output: False
```

## Explanation
### - Initialization:

* The function starts by checking if there are any boxes. If not, it returns False.
* It initializes an opened list to keep track of which boxes have been opened, starting with the first box (boxes[0]).
### Depth-First Search (DFS):

* A helper function dfs performs a depth-first search. It iterates over the keys in the current box and opens any box that hasn't been opened yet.
* DFS Call:

### The DFS starts from the first box (dfs(0)).
* Check Result:

* Finally, the function checks if all boxes have been opened using all(opened) and returns the result.
## Author
This project was developed by Efa Tariku(efatariku07@gmail.com).

License
This project is licensed under the MIT License - see the LICENSE file for details.
