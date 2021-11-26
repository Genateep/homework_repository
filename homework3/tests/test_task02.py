from time import time

from homework3.task02 import mult, slow_calculate


def test_mult_slow_calculate():
    start = time()
    mult(slow_calculate, [x for x in range(500)])
    end = time()

    assert end - start < 60
