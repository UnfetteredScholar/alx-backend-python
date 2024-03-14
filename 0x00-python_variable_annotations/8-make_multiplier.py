#!/usr/bin/env python3
"""Defines a type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier."""

    def multiplier_func(arg: float) -> float:
        return arg * multiplier

    return multiplier_func
