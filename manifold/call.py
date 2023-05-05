#!/usr/bin/env python3

from typing import Any, Callable, Hashable

from pysad.utils import hex_to_bytes

from manifold.signature import Signature


class Call:
    target: bytes
    signature: Signature
    input: tuple
    output_label: Hashable
    output_handler: Callable | None = None
    auto_unpack: bool  # auto-unpack decoded tuples with 1 element

    def __init__(
        self,
        target: str | bytes,
        function: str,
        input: tuple,
        output_label: Hashable,  # output label
        output_handler: Callable | None = None,  # optional post-processing function
        auto_unpack: bool = True,
    ):
        self.target = hex_to_bytes(target)
        self.signature = Signature(function)
        self.input = input
        self.output_label = output_label
        self.output_handler = output_handler

        self.auto_unpack = auto_unpack

    def encode(self) -> bytes:
        return self.signature.encode_input(self.input)

    def prepare(self) -> tuple[bytes, bytes]:
        return self.target, self.signature.selector + self.encode()

    def decode_output(self, success: bool, data: bytes) -> tuple[Hashable, Any]:
        if success is False:
            decoded_data = None
        else:
            try:
                decoded_data = self.signature.decode_output(data)
            except Exception:
                decoded_data = None
            else:
                if self.output_handler is not None:
                    decoded_data = self.output_handler(*data)
                elif len(decoded_data) == 1 and self.auto_unpack:
                    decoded_data = decoded_data[0]

        return (self.output_label, decoded_data)
