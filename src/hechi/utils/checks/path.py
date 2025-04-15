from __future__ import annotations

import os
from typing import Union
from pathlib import Path

from hechi.error import HechiOSError, HechiTypeError, HechiValueError


def check_python_module(file: Path):
    if not isinstance(file, Path):
        raise HechiTypeError(f"checks: python_module file must be Path but {type(file)}")

    if not (file.is_file() and file.suffix == ".py"):
        raise HechiValueError(
            (
                "The file '{}' is expected to be a Python file, but it is not a valid file or its extension is not .py"
            ).format(file)
        )


def check_destination(path: Path, /, create: bool = False):
    if not isinstance(path, Path):
        raise HechiTypeError(f"checks: destination path must be Path but {type(path)}")

    if path.is_dir():
        return
    elif not path.exists():
        if create:
            try:
                path.mkdir(parents=True)
            except Exception as error:
                raise HechiOSError(f"Failed to create directory: {error}")
        else:
            raise HechiValueError(f"The destination '{path}' does not exists.")
    else:
        raise HechiValueError(f"The destination '{path}' is not a valid directory. It is a file.")
