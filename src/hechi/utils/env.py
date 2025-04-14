import os
from typing import Any, Optional


class Env:
    """
    Wrapper for an environment variable that supports boolean evaluation.

    By default, all values are considered truthy unless explicitly set to a known falsy string:
    {"n", "no", "none", "false", "0"} (case-insensitive).

    Args:
        name (str): The name of the environment variable.
        default (Optional[Any]): The default value if the environment variable is not set.

    Example:
        >>> bool(Env("FEATURE_FLAG"))  # if FEATURE_FLAG="no"
        False
        >>> bool(Env("DEBUG"))  # if DEBUG is unset or set to "maybe"
        True
    """

    def __init__(self, name: str, default: Optional[Any] = None):
        self._value = os.getenv(name, default)

    def __bool__(self):
        """
        Evaluate the environment variable as a boolean.

        Returns:
            bool: False if the value is one of {"n", "no", "none", "false", "0"} (case-insensitive),
                  True otherwise.
        """
        return str(self._value).strip().lower() not in {"n", "no", "none", "false", "0"}
