#!/usr/bin/env python3
""" This is where to put the model Documentation"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Here is the coroutine documentation"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
