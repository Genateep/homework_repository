"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

# Example tree:
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


def find_occurrences(tree: dict, element: Any, count: int = 0) -> int:
    """Takes tree and element and finds the number of occurrences
    of this element in the tree

    :param tree: tree that can only contains basic structures like
        str, list, tuple, dict, set, int, bool
    :type tree: dict
    :param element: an object in tree to find
    :type element: str, list, tuple, dict, set, int, bool
    :param count: defaults to 0, used to counts occurrences recursively
    :type count: int
    :return: number of occurrences
    :rtype: int
    """
    if tree == element:
        count += 1
    elif isinstance(tree, (set, list, tuple)):
        for item in tree:
            count = find_occurrences(item, element, count)
    elif isinstance(tree, dict):
        for key, value in tree.items():
            count = find_occurrences(key, element, count)
            count = find_occurrences(value, element, count)
    return count


if __name__ == '__main__':
    print(find_occurrences(example_tree, "RED"))  # 6
