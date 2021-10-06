import sys
import textwrap

import pytest

from src.csvdiff3 import csvdiff


def test_option_k_not_specified(lhs, rhs, capfd):
    """ Run with column 0 as the matching key. """

    lhs.write(textwrap.dedent('''
        head1, head2, head3, head4, head5, head6
        0001, value1-2, key2-2, 1002, 20210921T035902, value4-2
        0001, value1-3, key2-3, 1003, 20210921T035904, value4-3
        0102, value1-4, key2-1, 1004, 20210924T180521, value4-e
        1003, value1-5, key2-1, 1005, 20210924T180528, value4-5
        1003, value1-6, key2-2, 1006, 20210923T143259, value4-6
        1003, value1-7, key2-3, 1007, 20210923T143258, value4-7
        1003, value1-e, key2-4, 1008, 20210923T143259, value4-8
    ''').strip())
    rhs.write(textwrap.dedent('''
        head1, head2, head3, head4, head5, head6
        0001, value1-1, key2-1, 1001, 20210921T035901, value4-1
        0001, value1-2, key2-2, 1002, 20210921T035902, value4-2
        0001, value1-3, key2-3, 1003, 20210921T035903, value4-3
        0102, value1-4e, key2-1, 1044, 20210924T180529, value4-4
        1003, value1-6, key2-2, 1006, 20210923T143259, value4-6
        1003, value1-8, key2-4, 1008, 20210923T143257, value4-e
    ''').strip())

    sys.argv = ['csvdiff.py', lhs.strpath, rhs.strpath, '-d']
    csvdiff.main()

    out, err = capfd.readouterr()
    assert err == ''
    assert out == textwrap.dedent('''
        ============ Report ============

        ● Differences
        --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        left.csv                                                                    right.csv                                                                   Column indices with difference
        --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        2 ['0001', 'value1-2', 'key2-2', '1002', '20210921T035902', 'value4-2']  !  2 ['0001', 'value1-1', 'key2-1', '1001', '20210921T035901', 'value4-1']   @ [1, 2, 3, 4, 5]
        3 ['0001', 'value1-3', 'key2-3', '1003', '20210921T035904', 'value4-3']  !  3 ['0001', 'value1-2', 'key2-2', '1002', '20210921T035902', 'value4-2']   @ [1, 2, 3, 4, 5]
                                                                                 >  4 ['0001', 'value1-3', 'key2-3', '1003', '20210921T035903', 'value4-3'] 
        4 ['0102', 'value1-4', 'key2-1', '1004', '20210924T180521', 'value4-e']  !  5 ['0102', 'value1-4e', 'key2-1', '1044', '20210924T180529', 'value4-4']  @ [1, 3, 4, 5]
        5 ['1003', 'value1-5', 'key2-1', '1005', '20210924T180528', 'value4-5']  !  6 ['1003', 'value1-6', 'key2-2', '1006', '20210923T143259', 'value4-6']   @ [1, 2, 3, 4, 5]
        6 ['1003', 'value1-6', 'key2-2', '1006', '20210923T143259', 'value4-6']  !  7 ['1003', 'value1-8', 'key2-4', '1008', '20210923T143257', 'value4-e']   @ [1, 2, 3, 4, 5]
        7 ['1003', 'value1-7', 'key2-3', '1007', '20210923T143258', 'value4-7']  <  
        8 ['1003', 'value1-e', 'key2-4', '1008', '20210923T143259', 'value4-8']  <  

    ''')

def test_option_u_specified(lhs, rhs, capfd):
    """
    Run the matching key as unique.
    So if it detects that the matching key is not unique, an error will occur.
    (Matching key duplication detection feature)
    """

    lhs.write(textwrap.dedent('''
        head1, head2, head3, head4, head5, head6
        0001, value1-2, key2-2, 1002, 20210921T035902, value4-2
        0001, value1-3, key2-3, 1003, 20210921T035904, value4-3
        0102, value1-4, key2-1, 1004, 20210924T180521, value4-e
        1003, value1-5, key2-1, 1005, 20210924T180528, value4-5
        1003, value1-6, key2-2, 1006, 20210923T143259, value4-6
        1003, value1-7, key2-3, 1007, 20210923T143258, value4-7
        1003, value1-e, key2-4, 1008, 20210923T143259, value4-8
    ''').strip())
    rhs.write(textwrap.dedent('''
        head1, head2, head3, head4, head5, head6
        0001, value1-1, key2-1, 1001, 20210921T035901, value4-1
        0001, value1-2, key2-2, 1002, 20210921T035902, value4-2
        0001, value1-3, key2-3, 1003, 20210921T035903, value4-3
        0102, value1-4e, key2-1, 1044, 20210924T180529, value4-4
        1003, value1-6, key2-2, 1006, 20210923T143259, value4-6
        1003, value1-8, key2-4, 1008, 20210923T143257, value4-e
    ''').strip())

    sys.argv = ['csvdiff.py', lhs.strpath, rhs.strpath, '-du']
    with pytest.raises(SystemExit) as e:
        csvdiff.main()

    assert e.type == SystemExit
    assert e.value.code == 1

    out, err = capfd.readouterr()
    assert str(err).find('are not unique.') > 0
    assert out == ''



