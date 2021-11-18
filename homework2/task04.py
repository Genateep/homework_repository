from typing import Callable


def cache(func: Callable) -> Callable:
    """Accepts another function as an argument. Then it
    should return such a function, so the every call to initial one
    should be cached"""
    memo = {}

    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = func(*args)
            memo[args] = rv
            return rv

    return wrapper


def some_func(a, b: int) -> int:
    return (a ** b) ** 2
