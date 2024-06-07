#!/usr/bin/env python3
""" module doc """
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    :param lst: list of strings
    :return: a list of tuples
    """
    return [(i, len(i)) for i in lst]
