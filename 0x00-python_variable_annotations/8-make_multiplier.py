#!/usr/bin/env python3
"""
A type-annotated function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier.

    Parameters:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float
        and returns the result of multiplying it by the multiplier.
    """

    def multiplier_function(x: float) -> float:
        mul = x * multiplier
        return mul

    return multiplier_function
