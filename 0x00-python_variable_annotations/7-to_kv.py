#!/usr/bin/env python3
""" function to_kv that takes a string k and an int OR float v as arguments
and returns a tuple. The first element of the tuple is the string k.
2nd element is the square of the int/float v & should be annotated as a float.

"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """

    :param k: a string
    :param v: a (float or int) number
    :return: tuple 1st element is the string & 2nd is the square of the number
    """
    return k, float(v**2)
