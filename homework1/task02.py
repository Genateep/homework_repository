"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


# Check that sequence is Fibonacci sequence
def check_fib(data: Sequence[int]) -> bool:
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
