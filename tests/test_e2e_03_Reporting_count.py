import sys
import textwrap

from src.csvdiff3 import csvdiff


def test_show_number_of_cases(lhs, rhs, capfd):

    lhs.write(textwrap.dedent('''
        head1, head2, head3, head4, head5, head6
        1, value1-2, key2-2, 1002, 20210921T035902, value4-2
        1, value1-3, key2-3, 1003, 20210921T035904, value4-3
        102, value1-4, key2-1, 1004, 20210924T180521, value4-e
        1003, value1-5, key2-1, 1005, 20210924T180528, value4-5
        1003, value1-6, key2-2, 1006, 20210923T143259, value4-6
        1003, value1-7, key2-3, 1007, 20210923T143258, value4-7
        1003, value1-e, key2-4, 1008, 20210923T143259, value4-8
    ''').strip())
    rhs.write(textwrap.dedent('''
        head1, head2, head3, head4, head5, head6
        1, value1-1, key2-1, 1001, 20210921T035901, value4-1
        1, value1-2, key2-2, 1002, 20210921T035902, value4-2
        1, value1-3, key2-3, 1003, 20210921T035903, value4-3
        102, value1-4e, key2-1, 1044, 20210924T180529, value4-4
        1003, value1-6, key2-2, 1006, 20210923T143259, value4-6
        1003, value1-8, key2-4, 1008, 20210923T143257, value4-e
    ''').strip())

    sys.argv = ['csvdiff.py', lhs.strpath, rhs.strpath, '-k0:4,2']
    csvdiff.main()

    out, err = capfd.readouterr()
    assert err == ''
    assert out == textwrap.dedent('''
        ============ Report ============

        ● Count & Row number
        same lines           : 2
        left side only    (<): 2 :-- Row Numbers      -->: [5, 7]
        right side only   (>): 1 :-- Row Numbers      -->: [2]
        with differences  (!): 3 :-- Row Number Pairs -->: [(3, 4), (4, 5), (8, 7)]
    ''')



