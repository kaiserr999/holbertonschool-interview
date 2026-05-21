#!/usr/bin/python3
"""
Module for Lockboxes
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    
    Args:
        boxes: A list of lists representing boxes and their keys.
        
    Returns:
        True if all boxes can be opened, else False.
    """
    if not boxes or type(boxes) is not list:
        return False

    n = len(boxes)
    unlocked = {0}
    stack = [0]

    while stack:
        current_box = stack.pop()
        
        for key in boxes[current_box]:
            if key < n and key not in unlocked:
                unlocked.add(key)
                stack.append(key)

    return len(unlocked) == n
