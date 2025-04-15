from __future__ import annotations
from typing import List, Type

from .abc import AbstractCommand
from .encrypt_file import EncryptFileCommand
from .license import LicenseCommand


COMMANDS: List[Type[AbstractCommand]] = [
    EncryptFileCommand,
    LicenseCommand,
]
