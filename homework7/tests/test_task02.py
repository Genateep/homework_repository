from homework7.task02 import backspace_compare


def test_backspace_compare_positive():
    assert backspace_compare("ab#c", "ad#c")
    assert backspace_compare("a##c", "#a#c")
    assert backspace_compare("#", "")
    assert backspace_compare("", "")


def test_backspace_compare_negative():
    assert not backspace_compare("a#c", "b")
    assert not backspace_compare("a##c", "#ac#")
