import pytest
from homework1.task02 import check_fib


def test_positive_case():
    """Testing that Fibonacci sequence give True"""
    assert check_fib([0, 1, 1, 2, 3, 5, 8, 13])


def test_negative_case():
    """Testing that not Fibonacci sequence give False"""
    assert not check_fib([1, 2, 3, 4, 5, 6, 7, 8])
