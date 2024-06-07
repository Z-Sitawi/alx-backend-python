#!/usr/bin/env python3
""" function sum_mixed_list which takes a list mxd_lst of integers and floats
    and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """

    :param mxd_lst: A list of float and int numbers
    :return: the sum of the floats
    """
    return sum(mxd_lst)
