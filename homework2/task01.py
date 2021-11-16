import re
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Finds 10 longest words from largest amount of unique symbols"""
    words = {}
    with open(file_path, encoding='unicode-escape') as f:
        decoded = re.sub(r'[^\w\d\s]+', '', f.read())
        for word in decoded.split():
            words[word] = len(set(word))
    s_tuples = sorted(words.items(), key=lambda item: item[1], reverse=True)
    res = [x[0] for x in s_tuples[:9]]
    return res


def get_rarest_char(file_path: str) -> str:
    """Finds rarest symbol for document"""
    chars = {}
    with open(file_path, encoding='unicode-escape') as f:
        for char in ''.join(f.read().split()):
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    res = sorted(chars.items(), key=lambda item: item[1])[0][0]
    return res


def count_punctuation_chars(file_path: str) -> int:
    """Counts every punctuation char"""
    count = 0
    with open(file_path, encoding='unicode-escape') as f:
        for char in ''.join(f.read().split()):
            if not (char.isdigit() or char.isalpha()):
                count += 1
    return count


def count_non_ascii_chars(file_path: str) -> int:
    """Counts every non ascii char"""
    count = 0
    with open(file_path, encoding='unicode-escape') as f:
        for char in ''.join(f.read().split()):
            if ord(char) > 127:
                count += 1
    return count


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Finds most common non ascii char for document"""
    non_ascii_chars = {}
    with open(file_path, encoding='unicode-escape') as f:
        for char in ''.join(f.read().split()):
            if ord(char) > 127:
                if char in non_ascii_chars:
                    non_ascii_chars[char] += 1
                else:
                    non_ascii_chars[char] = 1
    res = sorted(non_ascii_chars.items(), key=lambda item: item[1])[-1][0]
    return res
