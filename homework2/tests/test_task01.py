import pytest

from homework2.task01 import get_longest_diverse_words


@pytest.mark.parametrize(
    "file_path, ans",
    [
        ("source/data.txt", ['unmißverständliche',
                             'Bevölkerungsabschub',
                             'Kollektivschuldiger',
                             'Werkstättenlandschaft',
                             'Schicksalsfiguren',
                             'Selbstverständlich',
                             'Fingerabdrucks',
                             'Friedensabstimmung',
                             'außenpolitisch']
         )
    ]
)
def test_positive_case(file_path, ans):
    assert get_longest_diverse_words(file_path) == ans
