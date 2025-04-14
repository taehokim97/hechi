from __future__ import annotations

import argparse
import sys

import hechi
from hechi.commands import COMMANDS


logger = hechi.get_logger()
tracer = hechi.get_tracer()


def main():
    parser = argparse.ArgumentParser(
        "hechi",
        description="Protect your Python code easily with Hechi!",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    for command_cls in COMMANDS:
        command = command_cls()
        command.configure_parser(subparsers)

    try:
        args = parser.parse_args()
        args.handler(vars(**args))
    except SystemExit:
        logger.error("Error: failed-to-parse-arguments")
        sys.exit(1)
    except Exception as e:
        logger.error("Error: unexpected-exception")
        tracer.error(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
