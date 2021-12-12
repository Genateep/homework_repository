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
def test_find_maximal_subarray_sum(nums, k, ans):
    assert find_maximal_subarray_sum(nums, k) == ans


def test_find_maximal_subarray_sum_negative_case():
    assert not find_maximal_subarray_sum([100, 50], 1) == 50
