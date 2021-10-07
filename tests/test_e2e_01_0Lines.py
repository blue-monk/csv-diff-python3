import sys
import textwrap

import pytest

from src.csvdiff3 import csvdiff


@pytest.mark.filterwarnings("ignore:Sniffing failed")
def test_no_lines_on_both_sides_as_no_header(lhs, rhs, capfd, args):

    lhs.write(textwrap.dedent('''
    ''').strip())
    rhs.write(textwrap.dedent('''
    ''').strip())

    sys.argv = ['csvdiff.py', lhs.strpath, rhs.strpath, '-dc']
    csvdiff.main()

    out, err = capfd.readouterr()
    assert err == ''
    assert out == textwrap.dedent('''
        ============ Report ============

        ● Differences
        -------------------------------------------
        left.csv     right.csv    Column indices with difference
        -------------------------------------------

        ● Count & Row number
        same lines           : 0
        left side only    (<): 0 :-- Row Numbers      -->: []
        right side only   (>): 0 :-- Row Numbers      -->: []
        with differences  (!): 0 :-- Row Number Pairs -->: []
    ''')

def test_no_lines_on_both_sides_with_header(lhs, rhs, capfd):

    lhs.write(textwrap.dedent('''
        head1, head2, head3, head4, head5
    ''').strip())
    rhs.write(textwrap.dedent('''
        head1, head2, head3, head4, head5
    ''').strip())

    sys.argv = ['csvdiff.py', lhs.strpath, rhs.strpath, '-dc']
    csvdiff.main()

    out, err = capfd.readouterr()
    assert err == ''
    assert out == textwrap.dedent('''
        ============ Report ============

        ● Differences
        -------------------------------------------
        left.csv     right.csv    Column indices with difference
        -------------------------------------------

        ● Count & Row number
        same lines           : 0
        left side only    (<): 0 :-- Row Numbers      -->: []
        right side only   (>): 0 :-- Row Numbers      -->: []
        with differences  (!): 0 :-- Row Number Pairs -->: []
    ''')



