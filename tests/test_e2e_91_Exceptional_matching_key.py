import sys
import textwrap

import pytest

from src.csvdiff3 import csvdiff


def test_specified_non_numeric_value_for_matching_key_index(lhs, rhs, capfd):

    lhs.write(textwrap.dedent('''
        head1, head2, head3, head4
        key1-1, value1-1, value2-1, value3-1
        key1-2, value1-2, value2-2, value3-2
        key1-3, value1-3, value2-3, value3-3
    ''').strip())
    rhs.write(textwrap.dedent('''
        head1, head2, head3, head4
        key1-1, value1-1, value2-1, value3-1
        key1-2, value1-2, value2-2, value3-2
        key1-3, value1-3, value2-3, value3-3
    ''').strip())

    sys.argv = ['csvdiff.py', lhs.strpath, rhs.strpath, '-ko', '-d']
    with pytest.raises(SystemExit) as e:
        csvdiff.main()

    assert e.type == SystemExit
    assert e.value.code == 1

    _, err = capfd.readouterr()
    assert str(err).find('MATCHING_KEY_INDICES should be a number. See also help. [specified index=o]') > 0

def test_specified_non_numeric_value_for_matching_key_max_length(lhs, rhs, capfd):

    lhs.write(textwrap.dedent('''
        head1, head2, head3, head4
        1, value1-1, value2-1, value3-1
        12, value1-2, value2-2, value3-2
        103, value1-3, value2-3, value3-3
    ''').strip())
    rhs.write(textwrap.dedent('''
        head1, head2, head3, head4
        1, value1-1, value2-1, value3-1
        12, value1-2, value2-2, value3-2
        103, value1-3, value2-3, value3-3
    ''').strip())

    sys.argv = ['csvdiff.py', lhs.strpath, rhs.strpath, '-k0:B', '-d']
    with pytest.raises(SystemExit) as e:
        csvdiff.main()

    assert e.type == SystemExit
    assert e.value.code == 1

    _, err = capfd.readouterr()
    assert str(err).find('MATCHING_KEY_INDICES should be a number. See also help. [specified max_length=B]') > 0

def test_specified_out_of_range_index_for_matching_key_index_1(lhs, rhs, capfd):

    lhs.write(textwrap.dedent('''
        head1, head2, head3, head4
        key1-1, value1-1, value2-1, value3-1
        key1-2, value1-2, value2-2, value3-2
        key1-3, value1-3, value2-3, value3-3
    ''').strip())
    rhs.write(textwrap.dedent('''
        head1, head2, head3, head4
        key1-1, value1-1, value2-1, value3-1
        key1-2, value1-2, value2-2, value3-2
        key1-3, value1-3, value2-3, value3-3
    ''').strip())

    sys.argv = ['csvdiff.py', lhs.strpath, rhs.strpath, '-k4', '-d']
    with pytest.raises(SystemExit) as e:
        csvdiff.main()

    assert e.type == SystemExit
    assert e.value.code == 1

    _, err = capfd.readouterr()
    assert str(err).find("one of the indices specified for MATCHING_KEY_INDICES is out of range") > 0

def test_specified_out_of_range_index_for_matching_key_index_2(lhs, rhs, capfd):

    lhs.write(textwrap.dedent('''
        head1, head2, head3, head4
        key1-1, value1-1, value2-1, value3-1
        key1-2, value1-2, value2-2, value3-2
        key1-3, value1-3, value2-3, value3-3
    ''').strip())
    rhs.write(textwrap.dedent('''
        head1, head2, head3, head4
        key1-1, value1-1, value2-1, value3-1
        key1-2, value1-2, value2-2, value3-2
        key1-3, value1-3, value2-3, value3-3
    ''').strip())

    sys.argv = ['csvdiff.py', lhs.strpath, rhs.strpath, '-k0,4', '-d']
    with pytest.raises(SystemExit) as e:
        csvdiff.main()

    assert e.type == SystemExit
    assert e.value.code == 1

    _, err = capfd.readouterr()
    assert str(err).find("one of the indices specified for MATCHING_KEY_INDICES is out of range") > 0



