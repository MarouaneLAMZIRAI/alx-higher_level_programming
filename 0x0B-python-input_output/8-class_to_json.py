#!/usr/bin/python3
"""
Module that contains a function to return the dictionary
description with simple data structure for JSON serialization
of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: Dictionary description of the object.
    """
    return obj.__dict__


if __name__ == "__main__":
    pass
