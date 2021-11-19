from homework3.task02 import mult, slow_calculate


def test_mult_slow_calculate():
    assert mult(slow_calculate) < 60
