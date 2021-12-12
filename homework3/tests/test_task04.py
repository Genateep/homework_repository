from homework3.task04 import is_armstrong


def test_is_armstrong_number():
    assert is_armstrong(153), 'Is Armstrong number'


def test_is_not_armstrong_number():
    assert not is_armstrong(10), 'Is not Armstrong number'
