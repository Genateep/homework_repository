import pytest

from homework1.task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    "nums, k, ans",
    [
        ([1], 1, 1),
        ([1, 2, 3, 4, 5], 2, 9),
        ([1, -50, 0, -20, 10], 3, 10),
    ],
)
def test_positive_cases(nums, k, ans):
    assert find_maximal_subarray_sum(nums, k) == ans
