from typing import Callable

from custom_exceptions import OutOfRangeException

MIN_VALUE = 1
MAX_VALUE = 1000


def check_integrity(f: Callable):
    def decorator(*args, **kwargs):

        for arg in args[1:]:
            if not isinstance(arg, int):
                raise TypeError(f"Value is not integer: {arg}")
            if arg < MIN_VALUE or arg > MAX_VALUE:
                raise OutOfRangeException

        return f(*args, **kwargs)

    return decorator
