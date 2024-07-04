#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.
    Each box contains keys to other boxes, and the goal is to figure 
    out if we can unlock all the boxes starting from box 0.

    Args:
        boxes (List[List[int]]): A list of lists where each list represents 
        a box and contains the keys to other boxes.
    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """

    # Check if there are no boxes to work with
    if not boxes:
        return False

    # Number of boxes
    n = len(boxes)
    # Initialize a list to keep track of which boxes have been opened
    opened = [False] * n

    # The first box (index 0) is always unlocked
    opened[0] = True

    def dfs(box):
        """
        Perform a depth-first search to unlock boxes.
        Args:
            box (int): The index of the current box being processed.
        """
        # Iterate over the keys found in the current box
        for key in boxes[box]:
            # Check if the key is within the valid range and the box has not been opened yet
            if key < n and not opened[key]:
                opened[key] = True

                dfs(key)

    dfs(0)

    return all(opened)
