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
def test_positive_case1(file_path, ans):
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
def test_positive_case2(file_path, ans):
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
def test_positive_case3(file_path, ans):
    assert t.count_punctuation_chars(file_path) == int(ans)
