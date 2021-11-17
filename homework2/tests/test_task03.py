from homework2.task03 import combinations


def test_combinations():
    assert combinations([1, 2], [4], ["a", True, 3]) == [
        [1, 4, "a"],
        [1, 4, True],
        [1, 4, 3],
        [2, 4, "a"],
        [2, 4, True],
        [2, 4, 3],
    ]


def test_combinations_negative():
    assert not combinations([1, 2], [4], ["a", True, 3]) == [
        [1, 4],
        [1, "a"],
        [1, True],
        [1, 3],
        [2, 4],
        [2, "a"],
        [2, True],
        [2, 3],
    ]
