#!/usr/bin/env python3
"""
A type-annotated function add that takes two floats as arguments
"""


def add(a: float, b: float) -> float:
    """
    Adds two floats together and returns their sum as a float.

    Parameters:
        a (float): The first float.
        b (float): The second float.

    Returns:
        float: The sum of a and b.
    """
    c = a + b
    return c
