#!/usr/bin/python3
"""
Lockboxes module
"""


def canUnlockAll(boxes):
    """
    A function that checks if all boxes can be unlocked with the provided keys
    @boxes: A list of lists with each list containing keys to unlock
      corresponding indexes
    Return: A boolean indicating whether or not all boxes can be unlocked
    """
    locked_boxes = [x for x in range(0, len(boxes))]  # unopened boxes
    unused_keys = set([0])  # unique set of keys that have not been checked
    current_key = 0   # current box being checked
    while len(unused_keys) and len(locked_boxes):
        current_key = next(iter(unused_keys))   # Pick a random unused key
        unused_keys.remove(current_key)   # Remove it from unused keys
        while current_key is not None:
            if len(locked_boxes) == 0:
                return True
            current_key_box = boxes[current_key]
            if current_key in locked_boxes:
                locked_boxes.remove(current_key)
            else:
                # Opened box, break and get new key from outer loop
                break
            new_current_key = None
            for each_key in current_key_box:
                if each_key in locked_boxes:
                    if not new_current_key:
                        new_current_key = each_key
                    else:
                        unused_keys.add(each_key)
            current_key = new_current_key
    if len(locked_boxes):
        return False
    return True
