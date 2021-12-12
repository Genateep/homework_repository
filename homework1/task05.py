from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:

    """Returns the maximal sum of subarray with length <= k"""

    n = len(nums)

    if not 0 < k <= n:
        raise ValueError("Subarray must be between 0 and array")
    sub_sum = 0
    res = nums[0]

    for i in range(k):
        sub_sum = sub_sum + nums[i]
        cur_sum = sub_sum
        max_sum = sub_sum
        for j in range(i + 1, n):
            cur_sum = cur_sum + nums[j] - nums[j - i - 1]
            max_sum = max(max_sum, cur_sum)
        res = max(max_sum, res)
    return res
