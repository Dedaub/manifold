#!/usr/bin/env python3

from typing import Any, Callable

from pysad.utils import hex_to_bytes

from manifold.signature import Signature


class Call:
    target: bytes
    signature: Signature
    input: tuple
    output_label: str
    output_handler: Callable | None
    auto_unpack: bool  # auto-unpack decoded tuples with 1 element

    def __init__(
        self,
        target: str | bytes,
        function: str,
        input: tuple,
        output: str
        | tuple[str, Callable],  # output label, optional post-processing function
        auto_unpack: bool = True,
    ):
        self.target = hex_to_bytes(target)
        self.signature = Signature(function)
        self.input = input
        if isinstance(output, str):
            self.output_label = output
        else:
            self.output_label, self.output_handler = output

        self.auto_unpack = auto_unpack

    def encode(self) -> bytes:
        return self.signature.encode_input(self.input)

    def prepare(self) -> tuple[bytes, bytes]:
        return self.target, self.encode()

    def decode_output(self, success: bool, data: bytes) -> tuple[str, Any]:
        decoded_data: tuple | Any | None
        if success is False:
            decoded_data = None
        else:
            decoded_data = self.signature.decode_output(data)

            if self.output_handler is not None:
                decoded_data = self.output_handler(*data)
            elif len(decoded_data) == 1 and self.auto_unpack:
                decoded_data = decoded_data[0]

        return (self.output_label, decoded_data)
