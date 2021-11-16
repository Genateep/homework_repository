"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import re
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Finds 10 longest words from largest amount of unique symbols"""
    words = dict()
    with open(file_path, encoding='unicode-escape') as f:
        decoded = re.sub(r'[^\w\d\s]+', '', f.read())
        for word in decoded.split():
            words[word] = len(set(word))
    s_tuples = sorted(words.items(), key=lambda item: item[1], reverse=True)
    res = [x[0] for x in s_tuples[:9]]
    return res


def get_rarest_char(file_path: str) -> str:
    ...


def count_punctuation_chars(file_path: str) -> int:
    ...


def count_non_ascii_chars(file_path: str) -> int:
    ...


def get_most_common_non_ascii_char(file_path: str) -> str:
    # chars = dict()
    # with open(file, encoding='unicode-') as f:
    #     for
    #         for c in someString:
    #             if 0 <= ord(c) <= 127:
    #             # this is a ascii character.
    #             else:
    #         # this is a non-ascii character. Do something.
    ...
