#!/usr/bin/python3
"""
0-lockboxes.py module
"""


def canUnlockAll(boxes):
    """
    checks if all boxes have keys
    """
    unlocked = []
    package = len(boxes)
    keys = [0]

    while len(unlocked) != package and len(keys) != 0:
        for key in boxes[keys[0]]:
            if key not in unlocked and key not in keys and key < package:
                keys.append(key)
        unlocked.append(keys.pop(0))

    return len(unlocked) == package
