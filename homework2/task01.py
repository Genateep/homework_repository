"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import unicodedata
from typing import List


class Token:
    def __init__(self, kind, value):
        self.kind = kind
        self.value = value


def open_file(file_path, encoding='utf8', errors='ignore'):
    """Reads the file line by line and yields characters"""
    with open(file_path, encoding=encoding, errors=errors) as file:
        for line in file:
            for symbol in line:
                yield symbol


def tokenize(opener):
    """Tokenize words and symbols from file-iterator"""
    buffer = ''
    for symbol in opener:
        if unicodedata.category(symbol).startswith("L"):
            buffer += symbol
        elif unicodedata.category(symbol).startswith("P"):
            yield Token(kind='punctuation_char', value=symbol)
        else:
            if buffer:
                yield Token(kind='word', value=buffer)
                buffer = ''
            yield Token(kind='symbol', value=symbol)


def get_longest_diverse_words(
        file_path: str, encoding='utf8') -> List[str]:
    """Finds 10 longest words from largest amount of unique symbols"""
    words = set()
    for word in tokenize(open_file(file_path, encoding=encoding)):
        if word.kind != 'word':
            continue
        else:
            words.add(word.value)
    return sorted(words, key=lambda w: (len(w), w), reverse=True)[:10]


def get_rarest_char(file_path: str, encoding='utf8') -> str:
    """Finds rarest symbol for document"""
    chars = {}
    for char in open_file(file_path, encoding=encoding):
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    res = sorted(chars.items(), key=lambda item: item[1])[0][0]
    return res


def count_punctuation_chars(file_path: str, encoding='utf8') -> int:
    """Counts every punctuation char"""
    count = 0
    for punc in tokenize(open_file(file_path, encoding=encoding)):
        if punc.kind != 'punctuation_char':
            continue
        else:
            count += 1
    return count


def count_non_ascii_chars(file_path: str, encoding='utf8') -> int:
    """Counts every non ascii char"""
    count = 0
    for char in open_file(file_path, encoding=encoding):
        if ord(char) > 127:
            count += 1
    return count


def get_most_common_non_ascii_char(file_path: str, encoding='utf8') -> str:
    """Finds most common non ascii char for document"""
    non_ascii_chars = {}
    for char in open_file(file_path, encoding=encoding):
        if ord(char) > 127:
            if char in non_ascii_chars:
                non_ascii_chars[char] += 1
            else:
                non_ascii_chars[char] = 1
    res = sorted(non_ascii_chars.items(), key=lambda item: item[1])[-1][0]
    return res
