from typing import Callable


def cache(func: Callable) -> Callable:
    """Accepts another function as an argument. Then it
    should return such a function, so the every call to initial one
    should be cached"""
    cached = dict()

    def decorate(*args, **kwargs):
        key = (tuple(args), hash(tuple(sorted(kwargs.items()))))
        if key not in cached:
            cached[key] = func(*args, **kwargs)
        return cached[key]

    return decorate


def some_func(a, b: int) -> int:
    return (a ** b) ** 2
