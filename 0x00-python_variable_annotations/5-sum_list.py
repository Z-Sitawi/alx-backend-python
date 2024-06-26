#!/usr/bin/env python3
""" function sum_list which takes a list input_list of floats as argument
    and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """

    :param input_list: A list of floats
    :return: the sum of the floats
    """
    return float(sum(input_list))
