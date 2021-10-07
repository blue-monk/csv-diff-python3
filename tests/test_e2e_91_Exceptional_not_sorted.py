import sys
import textwrap

import pytest

from src.csvdiff3 import csvdiff


def test_string_matching_key_not_sorted(lhs, rhs, capfd):

    lhs.write(textwrap.dedent('''
        head1, head2, head3, head4
        key1-1, value1-1, value2-1, value3-1
        key1-2, value1-2, value2-2, value3-2
        key1-3, value1-3, value2-3, value3-3
    ''').strip())
    rhs.write(textwrap.dedent('''
        head1, head2, head3, head4
        key1-1, value1-1, value2-1, value3-1
        key1-3, value1-2, value2-2, value3-2
        key1-2, value1-3, value2-3, value3-3
    ''').strip())

    sys.argv = ['csvdiff.py', lhs.strpath, rhs.strpath, '-d']
    with pytest.raises(SystemExit) as e:
        csvdiff.main()

    assert e.type == SystemExit
    assert e.value.code == 1

    _, err = capfd.readouterr()
    assert str(err).find("are not sorted. [current_key=['key1-2'], previous_key=['key1-3']") > 0

def test_numerical_matching_key_not_sorted(lhs, rhs, capfd):

    lhs.write(textwrap.dedent('''
        head1, head2, head3, head4
        1, value1-1, value2-1, value3-1
        103, value1-3, value2-3, value3-3
        12, value1-2, value2-2, value3-2
    ''').strip())
    rhs.write(textwrap.dedent('''
        head1, head2, head3, head4
        1, value1-1, value2-1, value3-1
        12, value1-2, value2-2, value3-2
        103, value1-3, value2-3, value3-3
    ''').strip())

    sys.argv = ['csvdiff.py', lhs.strpath, rhs.strpath, '-k0:3', '-d']
    with pytest.raises(SystemExit) as e:
        csvdiff.main()

    assert e.type == SystemExit
    assert e.value.code == 1

    _, err = capfd.readouterr()
    assert str(err).find("are not sorted. [current_key=['012'], previous_key=['103']") > 0



