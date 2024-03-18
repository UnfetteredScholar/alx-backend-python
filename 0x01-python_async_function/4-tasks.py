#!/usr/bin/env python3
"""Defines a function task_wait_random"""
import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Creates an asyncio.Task for wait_random"""

    times = await asyncio.gather(
        *[task_wait_random(max_delay) for _ in range(0, n)]
    )

    return sorted(times)
