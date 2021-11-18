from homework3.task01 import some_func


def test_some_func():
    a, b, c, d, e = (some_func(15, 6) for _ in range(5))
    assert a is b and b is c and c is not d and d is not e
