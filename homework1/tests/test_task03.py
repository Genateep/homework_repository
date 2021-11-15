import pytest

from homework1.task03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    "file_name, min_num, max_num",
    [
        ("https://github.com/Genateep/homework_repository/blob/hw1/homework1/tests/some_file.txt", -1, 7),
        # ("another_file.txt", (0, 9))
    ]
)
def test_positive_case(file_name, min_num, max_num):
    assert find_maximum_and_minimum(file_name) == (min_num, max_num)
