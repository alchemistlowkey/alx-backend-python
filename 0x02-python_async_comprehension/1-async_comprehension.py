#!/usr/bin/env python3
"""
Import async_generator from the previous task and
then write a coroutine called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehensing
over async_generator, then return the 10 random numbers.
"""
import asyncio
import random

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Coroutine that collects 10 random numbers
    using async comprehension over async_generator.

    Returns:
        list: A list containing 10 random integers between 0 and 10.
    """
    random_numbers = [number async for number in async_generator()]
    return random_numbers
