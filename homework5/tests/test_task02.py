import pytest

from homework5.task02 import custom_sum


@pytest.mark.parametrize(
    ["args", "ans"],
    [
        (([1, 2, 3], [4, 5]), [1, 2, 3, 4, 5]),
        ((1, 2, 3, 4), 10),
    ],
)
def test_custom_sum(capsys, args, ans):
    custom_sum(*args)
    without_print = custom_sum.__original_func
    captured = capsys.readouterr()

    assert str(ans) in captured.out
    assert custom_sum.__doc__ == custom_sum.__doc__
    assert custom_sum.__name__ == custom_sum.__name__

    # the result returns without printing
    assert without_print(*args) == ans
