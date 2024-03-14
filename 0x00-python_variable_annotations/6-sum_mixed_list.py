#!/usr/bin/env python3
from typing import List, Union

"""Defines the annotated function sum_mixed_list"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list mxd_lst of integers and
    floats and returns their sum as a float.
    """
    return sum(mxd_lst, start=0.0)
