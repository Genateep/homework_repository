import pytest

from homework2 import task01 as t


@pytest.mark.parametrize(
    "file_path, ans",
    [
        (
            "homework2/tests/source/data.txt",
            [
                "unmißverständliche",
                "Bevölkerungsabschub",
                "Kollektivschuldiger",
                "Werkstättenlandschaft",
                "Schicksalsfiguren",
                "Selbstverständlich",
                "Fingerabdrucks",
                "Friedensabstimmung",
                "außenpolitisch",
            ],
        )
    ],
)
def test_get_longest_diverse_words(file_path, ans):
    assert t.get_longest_diverse_words(file_path) == ans


@pytest.mark.parametrize(
    "file_path, ans",
    [
        (
            "homework2/tests/source/data.txt",
            [
                '›', '‹', 'Y', 'î', '’', 'X', '(', ')',
            ],
        )
    ],
)
def test_get_rarest_char(file_path, ans):
    assert t.get_rarest_char(file_path) in ans


@pytest.mark.parametrize(
    "file_path, ans",
    [
        (
            "homework2/tests/source/data.txt",
            "5475",
        )
    ],
)
def test_count_punctuation_chars(file_path, ans):
    assert t.count_punctuation_chars(file_path) == int(ans)


@pytest.mark.parametrize(
    "file_path, ans",
    [
        (
            "homework2/tests/source/data.txt",
            "2972",
        )
    ],
)
def test_count_non_ascii_chars(file_path, ans):
    assert t.count_non_ascii_chars(file_path) == int(ans)


@pytest.mark.parametrize(
    "file_path, ans",
    [
        (
            "homework2/tests/source/data.txt",
            "ä",
        )
    ],
)
def test_get_most_common_non_ascii_char(file_path, ans):
    assert t.get_most_common_non_ascii_char(file_path) == ans
