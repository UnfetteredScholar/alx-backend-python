#!/usr/bin/env python3

"""
Defines the function async_generator
"""
import asyncio
import random
from typing import Iterator


async def async_generator() -> Iterator[float]:
    """
    The coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10. Use the random module.
    """
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)