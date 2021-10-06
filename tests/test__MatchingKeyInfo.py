import pytest

from src.csvdiff3.csvdiff import MatchingKeyInfo


class Expected:

    def __init__(self, index, max_length):
        self.index = index
        self.max_length = max_length

class RowAndExpectedManagedKey:

    def __init__(self, row, expected_managed_key):
        self.row = row
        self.expected_managed_key = expected_managed_key


@pytest.mark.parametrize(
    "specified_matching_key, expected, row_and_expected_managed_key_pair",
    [
        pytest.param('0',   Expected(index=0, max_length=0), RowAndExpectedManagedKey(['key1', 'value1'],         expected_managed_key='key1'),      id='index only case-1'),
        pytest.param('2',   Expected(index=2, max_length=0), RowAndExpectedManagedKey(['key1', 'value1', 'key2'], expected_managed_key='key2'),      id='index only case-2'),
        pytest.param('0:9', Expected(index=0, max_length=9), RowAndExpectedManagedKey(['1', 'value1'],            expected_managed_key='000000001'), id='index and max length with 1 digit'),
        pytest.param('0:9', Expected(index=0, max_length=9), RowAndExpectedManagedKey(['123456789', 'value1'],    expected_managed_key='123456789'), id='index and max length with full digits'),
        pytest.param('0:9', Expected(index=0, max_length=9), RowAndExpectedManagedKey(['12345678', 'value1'],     expected_managed_key='012345678'), id='index and max length with full digits - 1'),
        pytest.param('0:9', Expected(index=0, max_length=9), RowAndExpectedManagedKey(['abc', 'value1'],          expected_managed_key='000000abc'), id='index and max length with alphabet'),
    ],
)
def test_matching_key_info(specified_matching_key, expected, row_and_expected_managed_key_pair):

    sut = MatchingKeyInfo(specified_matching_key)

    assert sut.index == expected.index
    assert sut.max_length == expected.max_length
    assert sut.key_for(row_and_expected_managed_key_pair.row) == row_and_expected_managed_key_pair.expected_managed_key



