from homework2.task04 import cache, some_func


def test_cache():
    cache_func = cache(some_func)
    some = 100, 200
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2


def test_cache_negative():
    cache_func = cache(some_func)
    some = 1, 2
    another = 3, 4
    val_1 = cache_func(*some)
    val_2 = cache_func(*another)
    assert val_1 is not val_2
