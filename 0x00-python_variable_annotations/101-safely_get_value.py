#!/usr/bin/env python3
"""
Given the parameters & the return values, add type annotations to the function
Hint: look into TypeVar
"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] =
                     None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary.

    Parameters:
        dct (Mapping): The input dictionary.
        key (Any): The key to look up in the dictionary.
        default (Union[T, None], optional):
        The default value to return if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]:
            The value corresponding to the key in the dictionary if found,
            otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
