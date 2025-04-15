from abc import ABC, abstractmethod
from argparse import ArgumentParser, _SubParsersAction


class AbstractCommand(ABC):
    """
    Abstract base class for defining CLI commands.

    Each command must specify a `name` attribute, implement `configure_parser` to define
    its arguments, and implement `main` to handle execution logic.

    Attributes:
        name (str): The name of the command, used to register it with the argument parser.

    Methods:
        configure_parser(subparsers): Configure the command-specific argument parser.
        main(*args, **kwargs): Execute the command logic when invoked.
    """

    name: str

    @abstractmethod
    def configure_parser(self, subparsers: _SubParsersAction[ArgumentParser]) -> None:
        """
        Define and register the arguments for the command.

        Args:
            subparsers (_SubParsersAction[ArgumentParser]): The subparsers object used to add a new subcommand.
        """
        pass

    @abstractmethod
    def main(self, *args, **kwargs) -> None:
        """
        Execute the main logic for the command.

        Args:
            *args: Positional arguments passed to the command.
            **kwargs: Keyword arguments passed to the command.
        """
        pass


class BaseEncryptCommand(AbstractCommand):
    def configure_runtime_option(self, parser: ArgumentParser):
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
