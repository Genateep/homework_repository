from pathlib import Path

from homework9.task03 import universal_file_counter

dir_path = Path.cwd()


def test_count_lines():
    assert universal_file_counter(dir_path, 'txt') == 11


def test_count_words():
    assert universal_file_counter(dir_path, 'txt', str.split) == 12
