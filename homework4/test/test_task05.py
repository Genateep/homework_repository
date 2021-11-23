from homework4.task05 import fizzbuzz_gen


def test_fizzbuzz_gen_positive():
    assert list(fizzbuzz_gen(15)) == [
                '1',
                '2',
                'fizz',
                '4',
                'buzz',
                'fizz',
                '7',
                '8',
                'fizz',
                'buzz',
                '11',
                'fizz',
                '13',
                '14',
                'fizzbuzz',
            ]
