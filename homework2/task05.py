from typing import Any, Iterable


def custom_range(itr: Iterable[Any], *args) -> list:
    """Function that accepts any iterable of unique values and then
    it behaves as range function"""
    start, stop, step = 0, len(itr) - 1, 1

    if len(args) == 0:
        pass
    elif len(args) == 1:
        stop = itr.index(args[0])
    elif len(args) == 2:
        start, stop = itr.index(args[0]), itr.index(args[1])
    elif len(args) == 3:
        start, stop, step = itr.index(args[0]), itr.index(args[1]), args[2]
    else:
        raise TypeError("More than 4 arguments were passed in!")
    return list(itr)[start:stop:step]
