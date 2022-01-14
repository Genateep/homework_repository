from homework9.task02 import Suppressor, suppressor


def test_class_suppressor():
    with Suppressor(IndexError):
        assert [0][2]
    with Suppressor(ValueError):
        assert int('string')
    with Suppressor(KeyError):
        assert {"a": 1}["b"]


def test_generator_suppressor():
    with suppressor(IndexError):
        assert [0][2]
    with suppressor(ValueError):
        assert int('string')
    with suppressor(KeyError):
        assert {"a": 1}["b"]
