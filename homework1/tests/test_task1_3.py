import pytest

from homework1.task03 import find_maximum_and_minimum


def test_find_maximum_and_minimum():
    assert find_maximum_and_minimum("homework1/tests/source/some_file.txt") == (7, -1)


def test_find_maximum_and_minimum_negative_case():
    assert not find_maximum_and_minimum("homework1/tests/source/some_file.txt") == (1, 2)
