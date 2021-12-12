from collections import Counter
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """Finds the most common and the least common elements in array"""
    c = Counter(inp).most_common()
    most = c[0][0]
    least = c[-1][0]
    return most, least


print(major_and_minor_elem([3, 2, 3, 4, 1, 1, 1, 2, 1, 1]))
