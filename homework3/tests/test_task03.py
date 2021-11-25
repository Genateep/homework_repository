from homework3.task03 import *


def test_filter_key_error():
    """Key error bug fixed by .get method"""
    assert not make_filter(gender="male").apply(sample_data)


def test_keyword_filter_func():
    """Parameter name bug fixed"""
    assert make_filter(name="polly", type="bird").apply(sample_data) == [
        sample_data[1]
    ]


def test_late_binding_filter_func():
    """late binding problem fixed by adding parameters in keyword_filter_func"""
    additional = {"is_dead": False, "kind": "parrot", "type": "bird", "name": "polly"}
    assert make_filter(name="polly", type="bird").apply(sample_data) == [
        sample_data[1]
    ], [additional]
