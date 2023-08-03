#!/usr/bin/python3
"""function to try and unlocked boxes"""
from collections import deque


def canUnlockAll(boxes):
    """function to determine which boxes were open"""
    n = len(boxes)
    visited = set()
    queue = deque([0])

    while queue:
        box = queue.popleft()
        visited.add(box)

        for key in boxes[box]:
            if key not in visited and key < n:
                queue.append(key)
    return len(visited) == n
