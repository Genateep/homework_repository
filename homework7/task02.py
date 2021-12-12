"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: s = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""
import re


def backspace_compare(first: str, second: str) -> bool:
    """Returns if strings are equal when both are typed into
    empty text editors
    """
    f, s = [], []
    for char in first:
        if char != '#':
            f.append(char)
        elif f:
            f.pop()
    for char in second:
        if char != '#':
            s.append(char)
        elif s:
            s.pop()
    return f == s


def backspace_regexp_compare(first: str, second: str) -> bool:
    """Returns if strings are equal when both are typed into
    empty text editors
    """

    def _apply_backspace(s):
        while True:
            t = re.sub('.#', '', s, count=1)
            if len(s) == len(t):
                return re.sub('#+', '', t)
            s = t

    return _apply_backspace(first) == _apply_backspace(second)
