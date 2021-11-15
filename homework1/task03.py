from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:

    """Returns a tuple with the max and min values"""

    nums = set()

    with open(file_name) as fi:
        for line in fi:
            if len(line.strip()) > 0:
                nums.update(map(int, line.split()))

    return min(nums), max(nums)
