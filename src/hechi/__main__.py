from __future__ import annotations

import os
import argparse
import logging
import sys

import hechi


def main():
    logger = hechi.get_logger()

    parser = argparse.ArgumentParser(
        "hechi",
        description="Protect your Python code easily with Hechi!",
    )
    command_parser = parser.add_subparsers(dest="command", required=True)

    try:
        args = parser.parse_args()
    except argparse.ArgumentError as error:
        logger.error("Error: failed-to-parse-argument")
        sys.exit(1)


if __name__ == "__main__":
    main()
