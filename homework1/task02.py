from typing import Sequence


def check_fib(data: Sequence[int]) -> bool:

    """Returns if the given sequence is a Fibonacci sequence"""

    for i in data:
        if data.index(i) == 0 and i == 0:
            continue
        elif data.index(i) == 1 and i == 1:
            continue
        elif (
            data.index(i) > 1 and i == data[data.index(i) - 1] + data[data.index(i) - 2]
        ):
            continue
        else:
            return False

    return True
