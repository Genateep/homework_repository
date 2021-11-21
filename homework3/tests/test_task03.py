from homework3.task03 import *


def test_filter_key_error():
    try:
        assert make_filter(gender="male").apply(sample_data)
    except KeyError:
        return print(" KeyError bug")


def test_keyword_filter_func():
    assert not make_filter(name="polly", type="bird").apply(sample_data) == [
        sample_data[1]
    ], ""
