import sys
import textwrap

import pytest

from src.csvdiff3 import csvdiff


def test_1_lines_on_both_sides_as_no_header(lhs, rhs, capfd):

    lhs.write(textwrap.dedent('''
        key-1, value-1, value-2, value-3, value-4
    ''').strip())
    rhs.write(textwrap.dedent('''
        key-1, value-1, value-2, value-3, value-4
    ''').strip())

    sys.argv = ['csvdiff.py', lhs.strpath, rhs.strpath, '-dc', '-Hn']
    csvdiff.main()

    out, err = capfd.readouterr()
    assert err == ''
    assert out == textwrap.dedent('''
        ============ Report ============

        ● Differences
        -----------------------------------------------------------------------------------------------------------------------------------------------------
        left.csv                                                    right.csv                                                  Column indices with difference
        -----------------------------------------------------------------------------------------------------------------------------------------------------

        ● Count & Row number
        same lines           : 1
        left side only    (<): 0 :-- Row Numbers      -->: []
        right side only   (>): 0 :-- Row Numbers      -->: []
        with differences  (!): 0 :-- Row Number Pairs -->: []
    ''')

@pytest.mark.filterwarnings("ignore:Sniffing failed")
def test_1_lines_on_the_left_side_only_as_no_header(lhs, rhs, capfd):

    lhs.write(textwrap.dedent('''
        key-1, value-1, value-2, value-3, value-4
    ''').strip())
    rhs.write(textwrap.dedent('''
    ''').strip())

    sys.argv = ['csvdiff.py', lhs.strpath, rhs.strpath, '-dc', '-Hn']
    csvdiff.main()

    out, err = capfd.readouterr()
    assert err == ''
    assert out == textwrap.dedent('''
        ============ Report ============

        ● Differences
        ------------------------------------------------------------------------------------------------
        left.csv                                                    right.csv    Column indices with difference
        ------------------------------------------------------------------------------------------------
        1 ['key-1', 'value-1', 'value-2', 'value-3', 'value-4']  <  

        ● Count & Row number
        same lines           : 0
        left side only    (<): 1 :-- Row Numbers      -->: [1]
        right side only   (>): 0 :-- Row Numbers      -->: []
        with differences  (!): 0 :-- Row Number Pairs -->: []
    ''')

@pytest.mark.filterwarnings("ignore:Sniffing failed")
def test_1_lines_on_the_right_side_only_as_no_header(lhs, rhs, capfd):

    lhs.write(textwrap.dedent('''
    ''').strip())
    rhs.write(textwrap.dedent('''
        key-1, value-1, value-2, value-3, value-4
    ''').strip())

    sys.argv = ['csvdiff.py', lhs.strpath, rhs.strpath, '-dc', '-Hn']
    csvdiff.main()

    out, err = capfd.readouterr()
    assert err == ''
    assert out == textwrap.dedent('''
        ============ Report ============

        ● Differences
        ------------------------------------------------------------------------------------------------
        left.csv     right.csv                                                  Column indices with difference
        ------------------------------------------------------------------------------------------------
            >  1 ['key-1', 'value-1', 'value-2', 'value-3', 'value-4']

        ● Count & Row number
        same lines           : 0
        left side only    (<): 0 :-- Row Numbers      -->: []
        right side only   (>): 1 :-- Row Numbers      -->: [1]
        with differences  (!): 0 :-- Row Number Pairs -->: []
    ''')

def test_1_lines_on_both_sides_with_header(lhs, rhs, capfd):

    lhs.write(textwrap.dedent('''
        head1, head2, head3, head4, head5
        key-1, value-1, value-2, value-3, value-4
    ''').strip())
    rhs.write(textwrap.dedent('''
        head1, head2, head3, head4, head5
        key-1, value-1, value-2, value-3, value-4
    ''').strip())

    sys.argv = ['csvdiff.py', lhs.strpath, rhs.strpath, '-dc', '-Hy']
    csvdiff.main()

    out, err = capfd.readouterr()
    assert err == ''
    assert out == textwrap.dedent('''
        ============ Report ============

        ● Differences
        -----------------------------------------------------------------------------------------------------------------------------------------------------
        left.csv                                                    right.csv                                                  Column indices with difference
        -----------------------------------------------------------------------------------------------------------------------------------------------------

        ● Count & Row number
        same lines           : 1
        left side only    (<): 0 :-- Row Numbers      -->: []
        right side only   (>): 0 :-- Row Numbers      -->: []
        with differences  (!): 0 :-- Row Number Pairs -->: []
    ''')

@pytest.mark.filterwarnings("ignore:Sniffing failed")
def test_1_lines_on_the_left_side_only_with_header(lhs, rhs, capfd):

    lhs.write(textwrap.dedent('''
        head1, head2, head3, head4, head5
        key-1, value-1, value-2, value-3, value-4
    ''').strip())
    rhs.write(textwrap.dedent('''
    ''').strip())

    sys.argv = ['csvdiff.py', lhs.strpath, rhs.strpath, '-dc', '-Hy']
    csvdiff.main()

    out, err = capfd.readouterr()
    assert err == ''
    assert out == textwrap.dedent('''
        ============ Report ============

        ● Differences
        ------------------------------------------------------------------------------------------------
        left.csv                                                    right.csv    Column indices with difference
        ------------------------------------------------------------------------------------------------
        2 ['key-1', 'value-1', 'value-2', 'value-3', 'value-4']  <  

        ● Count & Row number
        same lines           : 0
        left side only    (<): 1 :-- Row Numbers      -->: [2]
        right side only   (>): 0 :-- Row Numbers      -->: []
        with differences  (!): 0 :-- Row Number Pairs -->: []
    ''')

@pytest.mark.filterwarnings("ignore:Sniffing failed")
def test_1_lines_on_the_right_side_only_with_header(lhs, rhs, capfd):

    lhs.write(textwrap.dedent('''
    ''').strip())
    rhs.write(textwrap.dedent('''
        head1, head2, head3, head4, head5
        key-1, value-1, value-2, value-3, value-4
    ''').strip())

    sys.argv = ['csvdiff.py', lhs.strpath, rhs.strpath, '-dc', '-Hy']
    csvdiff.main()

    out, err = capfd.readouterr()
    assert err == ''
    assert out == textwrap.dedent('''
        ============ Report ============

        ● Differences
        ------------------------------------------------------------------------------------------------
        left.csv     right.csv                                                  Column indices with difference
        ------------------------------------------------------------------------------------------------
            >  2 ['key-1', 'value-1', 'value-2', 'value-3', 'value-4']

        ● Count & Row number
        same lines           : 0
        left side only    (<): 0 :-- Row Numbers      -->: []
        right side only   (>): 1 :-- Row Numbers      -->: [2]
        with differences  (!): 0 :-- Row Number Pairs -->: []
    ''')



