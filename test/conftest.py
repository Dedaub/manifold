#!/usr/bin/env python3

import os

import pytest


@pytest.fixture
def eth_rpc_url() -> str:
    rpc_url = os.environ.get("ETH_RPC_URL")
    if not rpc_url:
        pytest.skip("ETH_RPC_URL is not set")
    return rpc_url
