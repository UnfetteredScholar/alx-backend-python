#!/usr/bin/env python3
"""Defines an annotated function element_length"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns the a list of tuples (obj, len(obj)) for obj in a sequence"""
    return [(i, len(i)) for i in lst]
