"""
Write a function that takes directory path,
a file extension and an optional tokenizer.
It will count lines in all files with that extension
if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
# >>> universal_file_counter(test_dir, "txt")
6
# >>> universal_file_counter(test_dir, "txt", str.split)
6

"""
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    """Counts lines in all files with specified extension
    if there are no tokenizer.
    If a the tokenizer is not none, it will count tokens.
    """
    counter = 0
    tokenizer = tokenizer or str.splitlines
    content_list = [
        path.read_text()
        for path in dir_path.rglob('*.' + file_extension)
    ]
    for file in content_list:
        for _ in tokenizer(file):
            counter += 1
    return counter
