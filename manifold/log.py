#!/usr/bin/env python3

import logging
from typing import Literal

from rich.logging import RichHandler

LOGGER_NAME = "manifold"
LogLevel = Literal["CRITICAL", "FATAL", "ERROR", "WARNING", "INFO", "DEBUG"]


def setup_logger(level: LogLevel):
    logger = logging.getLogger(LOGGER_NAME)
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.setLevel(level)
    logger.addHandler(RichHandler(rich_tracebacks=True))
    return logger


def get_logger() -> logging.Logger:
    return logging.getLogger(LOGGER_NAME)
