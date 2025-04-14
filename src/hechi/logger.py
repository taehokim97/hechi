"""Hechi logging setup.

This module provides two loggers:

- `get_logger` for user-facing error messages (stderr).
- `get_tracer` for internal debug logs (stdout if HECHI_TRACE is enabled).

Each logger is initialized once on import using environment variables:

- `HECHI_ERROR` controls whether the user-facing logger is active.
- `HECHI_TRACE` controls whether the debug tracer is active.
"""

from __future__ import annotations

import logging
import os
import sys
from typing import Final, IO, Optional, Literal

from hechi.utils.env import Env

__all__ = ("getLogger", "getTracer")

LOGGER_ENV: Final[str] = "HECHI_ERROR"
TRACER_ENV: Final[str] = "HECHI_TRACE"
LOGGER_NAME: Final[str] = "hechi.error"
TRACER_NAME: Final[str] = "hechi.trace"


def get_logger():
    """Logger for user-facing error output (stderr)."""
    return logging.getLogger(LOGGER_NAME)


def get_tracer():
    """Logger for internal debugging and tracing (stdout if HECHI_TRACE)."""
    return logging.getLogger(TRACER_NAME)


def init_logger():
    "Initialize the user-facing error logger."
    fmt = "%(message)s"
    enabled = bool(Env(LOGGER_ENV, True))
    _init(LOGGER_NAME, logging.ERROR, sys.stderr, fmt, not enabled)


def init_tracer():
    "Initialize the internal tracer logger."
    fmt = "TRACE | %(asctime)s | %(levelname)s | %(message)s"
    enabled = not bool(Env(TRACER_ENV, False))
    _init(TRACER_NAME, logging.DEBUG, sys.stdout, fmt, not enabled)


def _init(name: str, level: logging._Level, stream: IO[str], fmt: str, disabled: bool = True):
    """Internal helper to configure a named logger."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False  # Prevent double logging via root logger

    handler = logging.StreamHandler(stream)
    handler.setFormatter(logging.Formatter(fmt))
    logger.addHandler(handler)

    logger.disabled = disabled


# Auto-initialize loggers on module import
init_logger()
init_tracer()
