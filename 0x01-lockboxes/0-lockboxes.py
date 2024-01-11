#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    - boxes (list of lists): Each box contains keys to other boxes.

    Returns:
    - bool: True if all boxes can be opened, else False.
    """
    # A set to keep track of the opened boxes
    opened_boxes = {0}

    # List to keep track of the boxes to explore
    to_explore = [0]

    # Iterate through the boxes to explore
    while to_explore:
        current_box = to_explore.pop()

        # Check keys in the current box
        for key in boxes[current_box]:
            # If the key opens a new box and that box hasn't been opened yet
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.add(key)
                to_explore.append(key)

    # Check if all boxes are opened
    return len(opened_boxes) == len(boxes)
