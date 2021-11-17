from homework2 import task01 as t

file = "homework2/tests/source/data.txt"


def test_get_longest_diverse_words():
    assert t.get_longest_diverse_words(file) == [
        "unmißverständliche",
        "Bevölkerungsabschub",
        "Kollektivschuldiger",
        "Werkstättenlandschaft",
        "Schicksalsfiguren",
        "Selbstverständlich",
        "Fingerabdrucks",
        "Friedensabstimmung",
        "außenpolitisch",
    ]


def test_get_rarest_char():
    assert t.get_rarest_char(file) in [
        "›",
        "‹",
        "Y",
        "î",
        "’",
        "X",
        "(",
        ")",
    ]


def test_count_punctuation_chars():
    assert t.count_punctuation_chars(file) == 5475


def test_count_non_ascii_chars():
    assert t.count_non_ascii_chars(file) == 2972


def test_get_most_common_non_ascii_char():
    assert t.get_most_common_non_ascii_char(file) == "ä"
