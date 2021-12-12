import functools
import pytest

from homework5.task02 import custom_sum, func_saver


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

    # the result returns without printing
    assert without_print(*args) == ans


def decorate_one_more(func):
    def print_result(func):
        @func_saver(func)  # saves func attrs and func code
        def wrapper(*args, **kwargs):
            """Function-wrapper which print result of an original function"""
            result = func(*args, **kwargs)
            print(result)
            return result

        return wrapper

    return print_result(func)


def custom_sum_undecorated(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


@pytest.fixture
def decorated():
    return decorate_one_more(custom_sum_undecorated)


def test_original_func_attribute(decorated):
    assert decorated.__original_func is custom_sum_undecorated


def test_name_doc(decorated):
    assert decorated.__name__ == custom_sum_undecorated.__name__
    assert decorated.__doc__ == custom_sum_undecorated.__doc__
