#!/usr/bin/env python3

from typing import Generator, TypeVar

T = TypeVar("T")


def batch(items: list[T], batch_size: int) -> Generator[list[T], None, None]:
    return (items[i : i + batch_size] for i in range(0, len(items), batch_size))
