"""
Write a function that takes a number N as an input
and returns N FizzBuzz numbers*
Write a doctest for that function.

Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests


assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15,
"Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """Takes a number N as an input and returns N FizzBuzz numbers
    >>> fizzbuzz(0) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    ValueError
    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']
    """
    res = []
    if n < 1:
        raise ValueError
    for number in range(1, n + 1):
        if number % 15 == 0:
            res.append('fizzbuzz')
        elif number % 3 == 0:
            res.append('fizz')
        elif number % 5 == 0:
            res.append('buzz')
        else:
            res.append(str(number))
    return res


if __name__ == '__main__':
    import doctest

    doctest.testmod()
