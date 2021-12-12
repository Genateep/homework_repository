from typing import Any, Iterable


def custom_range(
    itr: Iterable[Any],
    start: Any,
    stop: Any = None,
    step: int = 1,
) -> list:
    """Function that accepts any iterable of unique values and then
    it behaves as range function"""
    if not stop:
        start = 0
        stop = itr.index(start)
    else:
        start = itr.index(start)
        stop = itr.index(stop)

    return list(itr)[start:stop:step]
