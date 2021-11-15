from collections import defaultdict
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:

    """Computes how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero."""

    ref = defaultdict(int)

    for i in a:
        for j in b:
            ref[i + j] += 1
    count = 0

    for k in c:
        for l in d:
            count += ref[-k - l]
    return count
