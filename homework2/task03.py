from itertools import product
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    """Takes K lists as arguments and returns all possible
    lists of K items where the first element is from the first list,
    the second is from the second and so on"""
    return [list(x) for x in product(*args)]
