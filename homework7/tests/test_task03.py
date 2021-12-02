from typing import List

import pytest

from homework7.task03 import tic_tac_toe_checker


@pytest.mark.parametrize(
    ["board", "ans"],
    [
        pytest.param(
            [
                ["x", "-", "o"],
                ["-", "x", "o"],
                ["x", "o", "x"],
            ],
            "x wins!",
        ),
        pytest.param(
            [
                ["x", "o", "o"],
                ["-", "o", "x"],
                ["x", "o", "x"],
            ],
            "o wins!",
        ),
        pytest.param(
            [
                ["x", "x", "o"],
                ["o", "o", "x"],
                ["x", "o", "o"],
            ],
            "draw!",
        ),
        pytest.param(
            [
                ["x", "-", "o"],
                ["-", "x", "o"],
                ["x", "o", "-"],
            ],
            "unfinished!",
        ),
    ],
)
def test_tic_tac_toe_checker(board: List[list], ans: str):
    assert tic_tac_toe_checker(board) == ans
