#!/usr/bin/env python3
"""
Import wait_random from 0-basic_async_syntax.

Write a function (do not create an async function,
use the regular function syntax to do this) task_wait_random
that takes an integer max_delay and returns a asyncio.Task.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task object for wait_random coroutine.

    Args:
        max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
        asyncio.Task: A Task object for wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
