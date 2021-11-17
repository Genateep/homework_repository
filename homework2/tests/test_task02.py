from homework2.task02 import major_and_minor_elem


def test_major_and_minor_elem():
    assert major_and_minor_elem([3, 2, 3, 4, 1, 1, 1, 2, 1, 1]) == (1, 4)


def test_major_and_minor_elem_negative():
    assert not major_and_minor_elem([0, 0, 0, 0, 0, 1]) == (1, 0)
