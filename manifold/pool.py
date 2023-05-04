#!/usr/bin/env python3


# Used in place of a multiprocessing Pool
# when the size of the pool is 1, re-implement
# whatever methods are required to maintain a
# compatible interface


class SingletonPool:
    def __init__(self, *args, **kwargs):
        pass

    def map(self, *args) -> list:
        return list(map(*args))
