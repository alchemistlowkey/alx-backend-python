#!/usr/bin/env python3
"""
A type-annotated function sum_list which takes a list input_list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Parameters:
        input_list (List[float]): A list of floats.

    Returns:
        float: The sum of the floats in the input list.
    """
    return sum(input_list)
