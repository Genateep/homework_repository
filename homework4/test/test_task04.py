from homework4.task04 import fizzbuzz


def test_fizzbuzz_positive():
    assert fizzbuzz(15) == [
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
