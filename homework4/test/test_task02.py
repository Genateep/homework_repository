from unittest.mock import Mock
from urllib.request import URLError

import pytest

from homework4.task02 import count_dots_on_i

url = "https://mocked_url.com/"
html = "<html>\n<head>iiiii</head>\n<body>\niiiiii\n</body>\n</html>"
answer = 11


def test_count_dots_on_i_positive(monkeypatch):
    mocked_urlopen = Mock()
    mocked_urlopen().read.return_value = html
    monkeypatch.setattr("homework4.task02.urlopen", mocked_urlopen)
    assert count_dots_on_i(url) == answer


def test_count_dots_on_i_negative(monkeypatch):
    monkeypatch.setattr(
        "homework4.task02.urlopen",
        Mock(side_effect=URLError('any')),
    )
    with pytest.raises(ValueError, match=f"Unreachable {url}"):
        count_dots_on_i(url)
