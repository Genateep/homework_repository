import string

from homework2.task05 import custom_range


def test_custom_range():
    assert custom_range(string.ascii_lowercase, "p", "g", -2) == [
        "p",
        "n",
        "l",
        "j",
        "h",
    ]


def test_custom_range_negative():
    assert not custom_range([x for x in range(10)], 5) == [0, 1, 2, 3, 4, 5]
