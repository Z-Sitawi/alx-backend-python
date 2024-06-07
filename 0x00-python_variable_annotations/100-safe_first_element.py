#!/usr/bin/env python3
""" Module documentation """
from typing import Optional, TypeVar, List

T = TypeVar('T')


def safe_first_element(lst: List[T]) -> Optional[T]:
    """Returns the first element of the list if it exists, otherwise returns None."""
    if lst:
        return lst[0]
    else:
        return None
