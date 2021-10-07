import sys
import textwrap

import pytest

from src.csvdiff3 import csvdiff


@pytest.mark.filterwarnings("ignore:Sniffing failed")
def test_different_number_of_columns_for_header_and_body(lhs, rhs, capfd):

    lhs.write(textwrap.dedent('''
        head1, head2, head3, head4, head5
        key1-1, value1-1, value2-1, value3-1
        key1-2, value1-2, value2-2, value3-2
        key1-3, value1-3, value2-3, value3-3
    ''').strip())
    rhs.write(textwrap.dedent('''
        head1, head2, head3, head4, head5
        key1-1, value1-1, value2-1, value3-1
        key1-2, value1-2, value2-2, value3-2
        key1-3, value1-3, value2-3, value3-3
    ''').strip())

    sys.argv = ['csvdiff.py', lhs.strpath, rhs.strpath, '-d']
    with pytest.raises(SystemExit) as e:
        csvdiff.main()

    assert e.type == SystemExit
    assert e.value.code == 1

    _, err = capfd.readouterr()
    assert str(err).find('IndexError') > 0

@pytest.mark.filterwarnings("ignore:Sniffing failed")
def test_different_number_of_columns_between_rows_of_body(lhs, rhs, capfd):

    lhs.write(textwrap.dedent('''
        head1, head2, head3, head4
        key1-1, value1-1, value2-1, value3-1
        key1-2, value1-2, value2-2
        key1-3, value1-3, value2-3, value3-3
    ''').strip())
    rhs.write(textwrap.dedent('''
        head1, head2, head3, head4
        key1-1, value1-1, value2-1, value3-1
        key1-2, value1-2, value2-2, value3-2
        key1-3, value1-3, value2-3
    ''').strip())

    sys.argv = ['csvdiff.py', lhs.strpath, rhs.strpath, '-d']
    with pytest.raises(SystemExit) as e:
        csvdiff.main()

    assert e.type == SystemExit
    assert e.value.code == 1

    _, err = capfd.readouterr()
    assert str(err).find('IndexError') > 0



