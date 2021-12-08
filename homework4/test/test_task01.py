from os import F_OK, access

import pytest

from homework4.task01 import read_magic_number

temp = []  # Collects absolute paths of temporary files


@pytest.fixture(params=['1', '2.5'])
def make_test_file_true(tmp_path, request):
    global temp
    temp_dir = tmp_path / 'tests'
    temp_dir.mkdir()
    temp_file = temp_dir / 'tests.txt'
    content = request.param
    temp_file.write_text(content)
    path = temp_file.resolve()
    temp.append(path)
    yield path, temp_file, content
    temp_file.unlink()
    temp_dir.rmdir()


@pytest.fixture(params=['q', '-1', '3'])
def make_test_file_false(tmp_path, request):
    global temp
    temp_dir = tmp_path / 'tests'
    temp_dir.mkdir()
    temp_file = temp_dir / 'tests.txt'
    content = request.param
    temp_file.write_text(content)
    path = temp_file.resolve()
    temp.append(path)
    yield path, temp_file, content
    temp_file.unlink()
    temp_dir.rmdir()


def test_read_magic_number_positive(make_test_file_true):
    path, temp_file, content = make_test_file_true

    assert access(temp_file, F_OK)
    assert temp_file.read_text() == content
    assert read_magic_number(path)


def test_read_magic_number_negative(make_test_file_false):
    path, temp_file, content = make_test_file_false

    assert access(temp_file, F_OK)
    assert temp_file.read_text() == content
    assert not read_magic_number(path)


def test_temporary_files_not_exist():
    for path in temp:
        assert not access(path, F_OK)


def test_read_magic_number_error():
    with pytest.raises(ValueError):
        assert read_magic_number('nothing')
