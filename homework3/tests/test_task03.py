from homework3.task03 import *


def test_filter_key_error():
    try:
        assert make_filter(gender="male").apply(sample_data)
    except KeyError:
        print(" KeyError bug. Raises E for unsuitable items in a data row")


def test_keyword_filter_func():
    """Parameter name bug fixed, now the function works as declared"""
    assert make_filter(name="polly", type="bird").apply(sample_data) == [
        sample_data[1]
    ]
