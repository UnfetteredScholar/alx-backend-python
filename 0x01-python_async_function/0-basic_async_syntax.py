#!/usr/bin/env python3
"""
Defines an async function wait_random
"""
import random
import time


async def wait_random(max_delay: int = 10) -> float:
    """Waits a random amount of time between 0  and max_delay"""
    delay = random.uniform(0, max_delay)

    time.sleep(delay)
    return delay
