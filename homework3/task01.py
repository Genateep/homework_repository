from typing import Callable


def timed_cache(times: int):
    def cache(func: Callable) -> Callable:
        """Accepts another function as an argument. Then it
        should return such a function, so the every call to initial one
        should be cached for n times unless it receives any other arguments"""
        cached = dict()

        def decorate(*args, **kwargs):
            key = (tuple(args), hash(tuple(sorted(kwargs.items()))))
            if key not in cached:
                cached[key] = func(*args, **kwargs)
                cached['times'] = times
            else:
                cached['times'] -= 1
            if cached['times'] <= 0:
                return func(*args, **kwargs)
            return cached[key]

        return decorate

    return cache


@timed_cache(times=3)
def some_func(k: int, m: int) -> int:
    return k ** m
