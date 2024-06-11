#!/usr/bin/env python3
""" This is where to put the model Documentation"""
import random
import asyncio


async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 11)
