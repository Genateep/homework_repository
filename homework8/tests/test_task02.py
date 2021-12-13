from homework8.task02 import TableData

path = 'homework8/tests/example.sqlite'


def test_tabledata_len():
    with TableData(path, 'presidents') as presidents:
        assert len(presidents) == 3


def test_tabledata_contains():
    with TableData(path, 'presidents') as presidents:
        assert 'Trump' in presidents
        assert 'Lincoln' not in presidents


def test_tabledata_getitem():
    with TableData(path, 'presidents') as presidents:
        assert presidents['Trump'] == ('Trump', 1337, 'US')


def test_tabledata_iter():
    with TableData(path, 'presidents') as presidents:
        names, ages, countries = [], [], []
        for president in presidents:
            names.append(president['name'])
            ages.append(president['age'])
            countries.append(president['country'])
        assert names == ['Yeltsin', 'Trump', 'Big Man Tyrone']
        assert ages == [999, 1337, 101]
        assert countries == ['Russia', 'US', 'Kekistan']
