from typing import Sequence


def check_fib(data: Sequence[int]) -> bool:
    """Returns if the given sequence is a Fibonacci sequence"""

    for index, value in enumerate(data):

        if index in (0, 1):
            if index == value:
                continue
            return False
        if value != data[index - 1] + data[index - 2]:
            return False
    return True
