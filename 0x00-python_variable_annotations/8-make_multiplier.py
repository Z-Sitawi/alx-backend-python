#!/usr/bin/env python3
""" function make_multiplier that takes a float multiplier as argument
and returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies its argument
        by the given multiplier.
    """

    def mult(m: float) -> float:
        """ Multiplies the given number by the multiplier. """
        return m * multiplier

    return mult
