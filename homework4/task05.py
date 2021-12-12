"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


# >>> list(fizzbuzz(5))
# ["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""


def fizzbuzz_gen(n: int):
    """
    >>> list(fizzbuzz_gen(5))
    ['1', '2', 'fizz', '4', 'buzz']
    """
    for i in range(1, n + 1):
        yield {3: "fizz", 5: "buzz", 15: "fizzbuzz"}.get(
            15 * (not i % 15) or 5 * (not i % 5) or 3 * (not i % 3), str(i)
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
