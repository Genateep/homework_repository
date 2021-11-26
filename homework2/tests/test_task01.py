from homework2.task01 import (count_non_ascii_chars, count_punctuation_chars,
                              get_longest_diverse_words,
                              get_most_common_non_ascii_char, get_rarest_char)

file_path = "homework2/tests/source/data.txt"


def test_get_longest_diverse_words():
    assert get_longest_diverse_words(
        file_path,
        encoding='unicode-escape'
    ) == [
        'Verfassungsverletzungen',
        'politischstrategischen',
        'Wiederbelebungsübungen',
        'zoologischpolitischen',
        'Werkstättenlandschaft',
        'Geschichtsphilosophie',
        'Entscheidungsschlacht',
        'résistanceBewegungen',
        'politischtechnischen',
        'menschenfreundlichen'
    ]


def test_get_rarest_char():
    assert get_rarest_char(
        file_path,
        encoding='unicode-escape'
    ) == '›'


def test_count_punctuation_chars():
    assert count_punctuation_chars(
        file_path,
        encoding='unicode-escape'
    ) == 5475


def test_count_non_ascii_chars():
    assert count_non_ascii_chars(
        file_path,
        encoding='unicode-escape'
    ) == 2971


def test_get_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char(
        file_path,
        encoding='unicode-escape'
    ) == "ä"
