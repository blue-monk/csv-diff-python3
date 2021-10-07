import pytest

from src.csvdiff3.csvdiff import MatchingKeyCodec, MatchingKeyInfo


class EncodeExpected:

    def __init__(self, managed_key, indices):
        self.managed_key = managed_key
        self.indices = indices


@pytest.mark.parametrize(
    "matching_key_infos, row, expected",
    [
        pytest.param([MatchingKeyInfo('0')],                                                  ['key1', 'value1', 'value2'],                     EncodeExpected('..key1..',                      [0]),       id='encode 1 alphabetical key'),
        pytest.param([MatchingKeyInfo('0'), MatchingKeyInfo('2')],                            ['key1', 'value1', 'key2'],                       EncodeExpected('..key1..key2..',                [0, 2]),    id='encode 2 alphabetical keys'),
        pytest.param([MatchingKeyInfo('0:10')],                                               ['1', 'value1', 'value2'],                        EncodeExpected('..0000000001..',                [0]),       id='encode 1 number key without zero padding'),
        pytest.param([MatchingKeyInfo('0:10'), MatchingKeyInfo('2:4')],                       ['123456789', 'value1', '3'],                     EncodeExpected('..0123456789..0003..',          [0, 2]),    id='encode 2 number keys without zero padding'),
        pytest.param([MatchingKeyInfo('0:10'), MatchingKeyInfo('1'), MatchingKeyInfo('4:6')], ['123456789', 'key-2', 'value1', 'value2', '98'], EncodeExpected('..0123456789..key-2..000098..', [0, 1, 4]), id='encode 2 number keys and 1 alphabetical key'),
    ],
)
def test_encode(matching_key_infos, row, expected):

    sut = MatchingKeyCodec(matching_key_infos)
    assert sut.managed_key_for(row) == expected.managed_key
    assert sut.matching_key_indices == expected.indices




class DecodeExpected:

    def __init__(self, key_indices):
        self.key_indices = key_indices


@pytest.mark.parametrize(
    "managed_key, expected",
    [
        pytest.param('..key1..',                      DecodeExpected(['key1']),                          id='decode 1 alphabetical key'),
        pytest.param('..key1..key2..',                DecodeExpected(['key1', 'key2']),                  id='decode 2 alphabetical keys'),
        pytest.param('..0000000001..',                DecodeExpected(['0000000001']),                    id='decode 1 number key (original is without zero padding)'),
        pytest.param('..0123456789..0003..',          DecodeExpected(['0123456789', '0003']),            id='decode 2 number keys (original is without zero padding)'),
        pytest.param('..0123456789..key-2..000098..', DecodeExpected(['0123456789', 'key-2', '000098']), id='decode 2 number keys and 1 alphabetical key'),
    ],
)
def test_decode(managed_key, expected):

    assert MatchingKeyCodec.decode_key(managed_key) == expected.key_indices



