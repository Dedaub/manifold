#!/usr/bin/env python3
"""aggregate() with one process, without a node.

PL/Python embeds Python in PostgreSQL, where sys.executable is empty. On
Python 3.14 the ThreadPool of multiprocessing starts the resource tracker
process from sys.executable, so aggregate() must not use it.
"""

import asyncio
import threading
from multiprocessing import resource_tracker

from manifold.call import Call
from manifold.multicall import MultiCall

ADDRESS = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"


class FakeMultiCall(MultiCall):
    """Answers each call with its key, and records the worker thread."""

    def __init__(self, calls):
        super().__init__("http://localhost:1/unused", calls, batch_size=2)
        self.threads: list[str] = []

    def multicall_worker(self, calls):
        self.threads.append(threading.current_thread().name)
        return [(call.output_label, call.output_label) for call in calls]


def calls(n: int) -> list[Call[int]]:
    return [Call(ADDRESS, "decimals()(uint8)", output_label=i) for i in range(n)]


def test_returns_every_result():
    assert FakeMultiCall(calls(5)).aggregate() == {i: i for i in range(5)}


def test_no_calls_gives_an_empty_result():
    assert FakeMultiCall([]).aggregate() == {}


def test_runs_in_a_worker_thread():
    multicall = FakeMultiCall(calls(3))
    multicall.aggregate()
    assert multicall.threads
    assert threading.main_thread().name not in multicall.threads


def test_works_when_the_caller_has_a_running_event_loop():
    async def caller():
        return FakeMultiCall(calls(3)).aggregate()

    assert asyncio.run(caller()) == {0: 0, 1: 1, 2: 2}


def test_does_not_start_the_resource_tracker():
    FakeMultiCall(calls(3)).aggregate()
    assert resource_tracker._resource_tracker._pid is None
