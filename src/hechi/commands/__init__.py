from __future__ import annotations
from typing import List, Type

from .abc import AbstractCommand
from .encrypt import EncryptCommand
from .license import LicenseCommand


COMMANDS: List[Type[AbstractCommand]] = [
    EncryptCommand,
    LicenseCommand,
]
