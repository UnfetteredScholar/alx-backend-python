#!/usr/bin/env python3
"""
Defines the function measure_time
"""
import asyncio
from time import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Determines the average execution time of wait_n(n, max_delay)"""

    start = time()
    asyncio.run(wait_n(n, max_delay))
    end = time()

    average_time = (end - start) / n

    return average_time
