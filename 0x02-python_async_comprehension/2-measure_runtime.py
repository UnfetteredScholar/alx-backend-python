#!/usr/bin/env python3
"""
Defines the function async_comprehension
"""
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of running
    async_comprehension 4 times in parallel
    """
    start = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    runtime = time.time() - start

    return runtime
