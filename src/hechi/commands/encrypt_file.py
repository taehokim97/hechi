from __future__ import annotations

from pathlib import Path
from typing import Literal, Optional

from hechi.utils.checks import (
    check_destination,
    check_python_module,
)

from .abc import BaseEncryptCommand


class EncryptFileCommand(BaseEncryptCommand):
    """
    A command that encrypts a single Python (.py) file.

    This command is used to encrypt an individual Python source file.
    The input file must have a `.py` extension. The encrypted output will be saved
    in the specified destination directory.

    Attributes:
        name (str): The command name used in the CLI (`encrypt-file`).
        help (str): A short description shown in `--help`.
        descriptions (str): A more detailed description shown in the CLI help section.

    CLI usage example:
        hechi encrypt-file main.py --dest ./output --runtime-py-version 311
    """

    name = "encrypt-file"
    help = "Encrypt a single Python (.py) file."
    descriptions = """
Encrypt a single Python (.py) file.

- The input file must end with `.py`.
- The encrypted output will be stored in the destination directory.
- You can optionally specify the target runtime environment (Python version, OS, architecture).
"""

    def configure_parser(self, subparsers):
        parser = subparsers.add_parser(self.name, help=self.help, description=self.descriptions)
        parser.set_defaults(handler=self.main)
        parser.add_argument("path", type=Path, help="Path to a single Python (.py) file to encrypt.")
        parser.add_argument(
            "--dest", type=Path, default="dest", help="Directory to store the encrypted output (default: ./dest)."
        )
        self.configure_runtime_option(parser)

    def main(
        self,
        path: Path,
        dest: Path,
        runtime_py_version: Optional[Literal["38", "39", "310", "311", "312"]],
        runtime_os: Optional[Literal["windows", "linux", "macos"]],
        runtime_arch: Literal["amd64"],
    ):
        check_python_module(path)
        check_destination(dest, create=True)

        utils.copyfile(path, dest)
