from homework9.task01 import merge_sorted_files as m_f


def test_merge_sorted_files():
    assert list(m_f(['file1.txt', 'file2.txt'])) == [1, 2, 3, 4, 5, 6]


def test_merge_sorted_files_negative_numbers():
    assert list(m_f(['file1.txt', 'file3.txt'])) == [-5, -3, -1, 1, 3, 5]


def test_merge_sorted_files_three_files():
    assert list(m_f(['file1.txt', 'file2.txt', 'file3.txt'])) == [
        -5,
        -3,
        -1,
        1,
        2,
        3,
        4,
        5,
        6,
    ]
