#!/usr/bin/env python3

from enum import IntEnum


class JSONRPCErrorCode(IntEnum):
    PARSE_ERROR = -32700
    INVALID_REQUEST = -32600
    METHOD_NOT_FOUND = -32601
    INVALID_PARAMS = -32602
    INTERNAL_ERROR = -32603
    INVALID_INPUT = -32000
    RESOURCE_NOT_FOUND = -32001
    RESOURCE_UNAVAILABLE = -32002
    TRANSACTION_REJECTED = -32003
    METHOD_NOT_SUPPORTED = -32004
    LIMIT_EXCEEDED = -32005
    VERSION_NOT_SUPPORTED = -32006


# https://eips.ethereum.org/EIPS/eip-1474#error-codes
EIP1474ErrorCodes = {item.value for item in JSONRPCErrorCode}


class JSONRPCError(RuntimeError):
    def __init__(self, code: int, message: str):
        super().__init__(message)
        self.code: int | JSONRPCErrorCode = (
            code if code not in EIP1474ErrorCodes else JSONRPCErrorCode(code)
        )


class HTTPException(RuntimeError):
    def __init__(self, status_code: int):
        self.status_code = status_code

    # Need this for pickle support
    def __reduce__(self):
        return type(self), (self.status_code,)
