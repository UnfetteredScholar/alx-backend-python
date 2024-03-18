#!/usr/bin/env python3
"""Defines the function wait_n"""
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n, max_delay):
    """
    Executes wait_random n times
    """
    results = await asyncio.gather(
        *[wait_random(max_delay) for _ in range(0, n)]
    )

    return sorted(results)
