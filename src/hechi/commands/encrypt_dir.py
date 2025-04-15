from __future__ import annotations

from typing import List, Literal, Optional

from .abc import AbstractCommand


class EncryptDirCommand(AbstractCommand):
    name = "encrypt"
    help = "Encrypt a .py file or all .py files inside a directory (copying all contents)."
    descriptions = """
Encrypt a single .py file or all .py files inside a given directory.

- If the input path is a file:
    - The file must end with `.py`.
    - Only that file will be encrypted.

- If the input path is a directory:
    - All files inside the directory will be **copied** to the destination directory.
    - Only files ending with `.py` will be **encrypted**.
    - You may customize which files to include or exclude using the flags below.

By default, common directories like `__pycache__` or hidden folders (starting with `.`) are excluded from scanning unless overridden.
"""

    def configure_parser(self, subparsers):
        parser = subparsers.add_parser(self.name, help=self.help, description=self.descriptions)
        parser.set_defaults(handler=self.main)
        parser.add_argument("path", help="A single file (.py) or directory to encrypt and/or copy.")
        parser.add_argument(
            "--dest", default="dest", help="Destination directory to store copied/encrypted files (default: ./dest)"
        )
        parser.add_argument(
            "--include",
            nargs="*",
            default=list(),
            help="File patterns to include (e.g. *.py, *.txt). Only used when path is a directory.",
        )
        parser.add_argument(
            "--exclude",
            nargs="*",
            default=list(),
            help="File or directory patterns to exclude. Only used when path is a directory.",
        )
        parser.add_argument(
            "--no-default-exclude",
            action="store_true",
            help="Disable default exclusion rules (e.g. '__pycache__', hidden folders).",
        )
        parser.add_argument(
            "--runtime-py-version",
            choices=["38", "39", "310", "311", "312"],
            default=None,
            help="Target Python runtime version (e.g. 38 for Python 3.8, 312 for Python 3.12). "
            "If not set, the current Python version is used.",
        )
        parser.add_argument(
            "--runtime-os",
            choices=["windows", "linux", "macos"],
            default=None,
            help="Target operating system. If not set, the current OS is used.",
        )
        parser.add_argument(
            "--runtime-arch", choices=["amd64"], default="amd64", help="Target system architecture (default: amd64)."
        )

    def main(
        self,
        path: str,
        dest: str,
        include: List[str],
        exclude: List[str],
        no_default_exclude: bool,
        runtime_py_version: Optional[Literal["38", "39", "310", "311", "312"]],
        runtime_os: Optional[Literal["windows", "linux", "macos"]],
        runtime_arch: Literal["amd64"],
    ):
        pass
