from typing import Any

import pytest

from homework7.task01 import find_occurrences

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
    },
    "fourth": "RED",
}


@pytest.mark.parametrize(
    ["tree", "element", "ans"],
    [
        pytest.param(example_tree, "first", 1),
        pytest.param(example_tree, "RED", 6),
        pytest.param(example_tree, "of", 2),
        pytest.param(example_tree, "abc", 1),
        pytest.param(example_tree, "nested_key", 1),
    ],
)
def test_example_tree(tree: dict, element: Any, ans: int):
    assert find_occurrences(tree, element) == ans
