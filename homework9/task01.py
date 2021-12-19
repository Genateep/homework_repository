"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>>> list(merge_sorted_files(["tests/file1.txt", "tests/file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from heapq import merge
from pathlib import Path
from typing import List, Union, Iterator


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    """Merges integers from sorted files and returns an iterator
    """
    data = (num for num in (map(int, item) for item in map(open, file_list)))
    yield from list(merge(*data))
