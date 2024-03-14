#!/usr/bin/env python3
"""
A type-annotated function floor which takes a float n as argument
"""
import math


def floor(n: float) -> int:
    """
    Returns the floor of the given float.

    Parameters:
        n (float): The input float.

    Returns:
        int: The floor value of the input float.
    """
    floorCalc = math.floor(n)
    return floorCalc
