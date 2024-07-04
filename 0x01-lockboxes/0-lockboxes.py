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
    
    if not isinstance(boxes, list):
        return False
    elif len(boxes) == 0:
        return False

    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = k in boxes[idx] and k != idx
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
