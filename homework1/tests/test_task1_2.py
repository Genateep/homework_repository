from homework1.task02 import check_fib


def test_check_fib_positive_case():
    """Testing that Fibonacci sequence give True"""
    assert check_fib([0, 1, 1, 2, 3, 5, 8, 13])
    assert check_fib([0, 1])


def test_check_fib_negative_case():
    """Testing that not Fibonacci sequence give False"""
    assert not check_fib([1, 2, 3, 4, 5, 6, 7, 8])
    assert not check_fib([1])
