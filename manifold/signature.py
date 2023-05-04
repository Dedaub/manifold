#!/usr/bin/env python3

from typing import Iterable

from eth_abi.abi import encode
from pysad.decoder import SignatureDecoder


class Signature(SignatureDecoder):
    def encode_input(self, input: Iterable) -> bytes:
        return encode(self.inputs, input)
