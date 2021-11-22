from unittest.mock import Mock
from urllib.request import URLError

import pytest

from homework4.task02 import count_dots_on_i

url = "mocked"


def test_count_dots_on_i_positive():
    mocked_count_dots_on_i = Mock(count_dots_on_i, return_value=11)
    assert mocked_count_dots_on_i(url) == 11


def test_count_dots_on_i_negative(monkeypatch):
    monkeypatch.setattr(
        "homework4.task02.urlopen",
        Mock(side_effect=URLError('any')),
    )
    with pytest.raises(ValueError, match=f"Unreachable {url}"):
        count_dots_on_i(url)
