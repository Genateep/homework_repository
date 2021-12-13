import pytest

from homework8.task01 import KeyValueStorage

PATH = 'task1.txt'
PATH2 = 'task1_2.txt'


def test_keyvaluestorage_items():
    storage = KeyValueStorage(PATH)
    assert storage["name"] == "kek"
    assert storage["last_name"] == "top"
    assert storage["power"] == 9001
    assert storage["song"] == "shadilay"


def test_keyvaluestorage_attributes():
    storage = KeyValueStorage(PATH)
    assert storage.name == "kek"
    assert storage.last_name == "top"
    assert storage.power == 9001
    assert storage.song == "shadilay"


def test_keyvaluestorage_builtins():
    with pytest.raises(ValueError):
        assert KeyValueStorage(PATH2)
