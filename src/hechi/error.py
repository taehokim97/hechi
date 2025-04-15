class HechiBaseError(BaseException):
    pass


class HechiOSError(HechiBaseError, OSError):
    pass


class HechiTypeError(HechiBaseError, TypeError):
    pass


class HechiValueError(HechiBaseError, ValueError):
    pass
