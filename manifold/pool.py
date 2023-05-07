#!/usr/bin/env python3

from itertools import starmap
from typing import Callable, Iterable, TypeVar

# Used in place of a multiprocessing Pool
# when the size of the pool is 1, re-implement
# whatever methods are required to maintain a
# compatible interface

TI = TypeVar("TI")
TO = TypeVar("TO")


class SingletonPool:
    def __init__(self, *args, **kwargs):
        pass

    def map(self, func: Callable[[TI], TO], args: Iterable[TI]) -> list[TO]:
        return list(map(func, args))

    def starmap(
        self, func: Callable[[tuple[TI]], TO], args: Iterable[tuple[TI]]
    ) -> list[TO]:
        return list(starmap(func, args))
