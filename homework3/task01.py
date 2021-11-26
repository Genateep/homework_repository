from typing import Callable


def timed_cache(times: int):
    """Accepts another function as an argument. Then it
    should return such a function, so the every call to initial one
    should be cached for n times unless it receives any other arguments"""
    cached, cached_times = {}, {}

    def cache(function: Callable):
        def decorate(*args, **kwargs):

            key = (tuple(args), hash(tuple(sorted(kwargs.items()))))

            if key in cached_times:
                res = cached[key]

                if cached_times[key] <= 1:
                    del cached_times[key]
                    del cached[key]
                else:
                    cached_times[key] -= 1
                return res
            res = function(*args, **kwargs)
            cached_times[key] = times
            cached[key] = res
            return res

        return decorate

    return cache


@timed_cache(times=3)
def some_func(k: int, m: int) -> int:
    return k ** m
