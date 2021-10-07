import sys
import textwrap

from src.csvdiff3 import csvdiff


def test_show_difference(lhs, rhs, capfd):

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

    sys.argv = ['csvdiff.py', lhs.strpath, rhs.strpath, '-k0:4,2', '-dv']
    csvdiff.main()

    out, err = capfd.readouterr()
    assert err == ''
    assert out == textwrap.dedent('''
        ============ Report ============

        ● Differences
        --------------------------------------------------------------------------------
        L left.csv
        R right.csv
        --------------------------------------------------------------------------------
        > R 2 ['1', 'value1-1', 'key2-1', '1001', '20210921T035901', 'value4-1']
        ! @ [4]
          L 3 ['1', 'value1-3', 'key2-3', '1003', '20210921T035904', 'value4-3']
          R 4 ['1', 'value1-3', 'key2-3', '1003', '20210921T035903', 'value4-3']
        ! @ [1, 3, 4, 5]
          L 4 ['102', 'value1-4', 'key2-1', '1004', '20210924T180521', 'value4-e']
          R 5 ['102', 'value1-4e', 'key2-1', '1044', '20210924T180529', 'value4-4']
        < L 5 ['1003', 'value1-5', 'key2-1', '1005', '20210924T180528', 'value4-5']
        < L 7 ['1003', 'value1-7', 'key2-3', '1007', '20210923T143258', 'value4-7']
        ! @ [1, 4, 5]
          L 8 ['1003', 'value1-e', 'key2-4', '1008', '20210923T143259', 'value4-8']
          R 7 ['1003', 'value1-8', 'key2-4', '1008', '20210923T143257', 'value4-e']

    ''')


def test_show_difference_and_number_of_cases(lhs, rhs, capfd):

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

    sys.argv = ['csvdiff.py', lhs.strpath, rhs.strpath, '-k0:4,2', '-dvc']
    csvdiff.main()

    out, err = capfd.readouterr()
    assert err == ''
    assert out == textwrap.dedent('''
        ============ Report ============

        ● Differences
        --------------------------------------------------------------------------------
        L left.csv
        R right.csv
        --------------------------------------------------------------------------------
        > R 2 ['1', 'value1-1', 'key2-1', '1001', '20210921T035901', 'value4-1']
        ! @ [4]
          L 3 ['1', 'value1-3', 'key2-3', '1003', '20210921T035904', 'value4-3']
          R 4 ['1', 'value1-3', 'key2-3', '1003', '20210921T035903', 'value4-3']
        ! @ [1, 3, 4, 5]
          L 4 ['102', 'value1-4', 'key2-1', '1004', '20210924T180521', 'value4-e']
          R 5 ['102', 'value1-4e', 'key2-1', '1044', '20210924T180529', 'value4-4']
        < L 5 ['1003', 'value1-5', 'key2-1', '1005', '20210924T180528', 'value4-5']
        < L 7 ['1003', 'value1-7', 'key2-3', '1007', '20210923T143258', 'value4-7']
        ! @ [1, 4, 5]
          L 8 ['1003', 'value1-e', 'key2-4', '1008', '20210923T143259', 'value4-8']
          R 7 ['1003', 'value1-8', 'key2-4', '1008', '20210923T143257', 'value4-e']
        
        ● Count & Row number
        same lines           : 2
        left side only    (<): 2 :-- Row Numbers      -->: [5, 7]
        right side only   (>): 1 :-- Row Numbers      -->: [2]
        with differences  (!): 3 :-- Row Number Pairs -->: [(3, 4), (4, 5), (8, 7)]
    ''')

def test_show_all_and_number_of_cases(lhs, rhs, capfd):

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

    sys.argv = ['csvdiff.py', lhs.strpath, rhs.strpath, '-k0:4,2', '-avc']
    csvdiff.main()

    out, err = capfd.readouterr()
    assert err == ''
    assert out == textwrap.dedent('''
        ============ Report ============

        ● All
        --------------------------------------------------------------------------------
        L left.csv
        R right.csv
        --------------------------------------------------------------------------------
        > R 2 ['1', 'value1-1', 'key2-1', '1001', '20210921T035901', 'value4-1']
        =
          L 2 ['1', 'value1-2', 'key2-2', '1002', '20210921T035902', 'value4-2']
          R 3 ['1', 'value1-2', 'key2-2', '1002', '20210921T035902', 'value4-2']
        ! @ [4]
          L 3 ['1', 'value1-3', 'key2-3', '1003', '20210921T035904', 'value4-3']
          R 4 ['1', 'value1-3', 'key2-3', '1003', '20210921T035903', 'value4-3']
        ! @ [1, 3, 4, 5]
          L 4 ['102', 'value1-4', 'key2-1', '1004', '20210924T180521', 'value4-e']
          R 5 ['102', 'value1-4e', 'key2-1', '1044', '20210924T180529', 'value4-4']
        < L 5 ['1003', 'value1-5', 'key2-1', '1005', '20210924T180528', 'value4-5']
        =
          L 6 ['1003', 'value1-6', 'key2-2', '1006', '20210923T143259', 'value4-6']
          R 6 ['1003', 'value1-6', 'key2-2', '1006', '20210923T143259', 'value4-6']
        < L 7 ['1003', 'value1-7', 'key2-3', '1007', '20210923T143258', 'value4-7']
        ! @ [1, 4, 5]
          L 8 ['1003', 'value1-e', 'key2-4', '1008', '20210923T143259', 'value4-8']
          R 7 ['1003', 'value1-8', 'key2-4', '1008', '20210923T143257', 'value4-e']
        
        ● Count & Row number
        same lines           : 2
        left side only    (<): 2 :-- Row Numbers      -->: [5, 7]
        right side only   (>): 1 :-- Row Numbers      -->: [2]
        with differences  (!): 3 :-- Row Number Pairs -->: [(3, 4), (4, 5), (8, 7)]
    ''')

def test_show_all_and_number_of_cases_with_ignore_column(lhs, rhs, capfd):

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

    sys.argv = ['csvdiff.py', lhs.strpath, rhs.strpath, '-k0:4,2', '-avc', '-i1']
    csvdiff.main()

    out, err = capfd.readouterr()
    assert err == ''
    assert out == textwrap.dedent('''
        ============ Report ============

        ● All
        --------------------------------------------------------------------------------
        L left.csv
        R right.csv
        --------------------------------------------------------------------------------
        > R 2 ['1', 'value1-1', 'key2-1', '1001', '20210921T035901', 'value4-1']
        =
          L 2 ['1', 'value1-2', 'key2-2', '1002', '20210921T035902', 'value4-2']
          R 3 ['1', 'value1-2', 'key2-2', '1002', '20210921T035902', 'value4-2']
        ! @ [4]
          L 3 ['1', 'value1-3', 'key2-3', '1003', '20210921T035904', 'value4-3']
          R 4 ['1', 'value1-3', 'key2-3', '1003', '20210921T035903', 'value4-3']
        ! @ [3, 4, 5]
          L 4 ['102', 'value1-4', 'key2-1', '1004', '20210924T180521', 'value4-e']
          R 5 ['102', 'value1-4e', 'key2-1', '1044', '20210924T180529', 'value4-4']
        < L 5 ['1003', 'value1-5', 'key2-1', '1005', '20210924T180528', 'value4-5']
        =
          L 6 ['1003', 'value1-6', 'key2-2', '1006', '20210923T143259', 'value4-6']
          R 6 ['1003', 'value1-6', 'key2-2', '1006', '20210923T143259', 'value4-6']
        < L 7 ['1003', 'value1-7', 'key2-3', '1007', '20210923T143258', 'value4-7']
        ! @ [4, 5]
          L 8 ['1003', 'value1-e', 'key2-4', '1008', '20210923T143259', 'value4-8']
          R 7 ['1003', 'value1-8', 'key2-4', '1008', '20210923T143257', 'value4-e']
        
        ● Count & Row number
        same lines           : 2
        left side only    (<): 2 :-- Row Numbers      -->: [5, 7]
        right side only   (>): 1 :-- Row Numbers      -->: [2]
        with differences  (!): 3 :-- Row Number Pairs -->: [(3, 4), (4, 5), (8, 7)]
    ''')


def test_show_all_and_number_of_cases_with_ignore_columns(lhs, rhs, capfd):

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

    sys.argv = ['csvdiff.py', lhs.strpath, rhs.strpath, '-k0:4,2', '-avc', '-i1,4']
    csvdiff.main()

    out, err = capfd.readouterr()
    assert err == ''
    assert out == textwrap.dedent('''
        ============ Report ============

        ● All
        --------------------------------------------------------------------------------
        L left.csv
        R right.csv
        --------------------------------------------------------------------------------
        > R 2 ['1', 'value1-1', 'key2-1', '1001', '20210921T035901', 'value4-1']
        =
          L 2 ['1', 'value1-2', 'key2-2', '1002', '20210921T035902', 'value4-2']
          R 3 ['1', 'value1-2', 'key2-2', '1002', '20210921T035902', 'value4-2']
        =
          L 3 ['1', 'value1-3', 'key2-3', '1003', '20210921T035904', 'value4-3']
          R 4 ['1', 'value1-3', 'key2-3', '1003', '20210921T035903', 'value4-3']
        ! @ [3, 5]
          L 4 ['102', 'value1-4', 'key2-1', '1004', '20210924T180521', 'value4-e']
          R 5 ['102', 'value1-4e', 'key2-1', '1044', '20210924T180529', 'value4-4']
        < L 5 ['1003', 'value1-5', 'key2-1', '1005', '20210924T180528', 'value4-5']
        =
          L 6 ['1003', 'value1-6', 'key2-2', '1006', '20210923T143259', 'value4-6']
          R 6 ['1003', 'value1-6', 'key2-2', '1006', '20210923T143259', 'value4-6']
        < L 7 ['1003', 'value1-7', 'key2-3', '1007', '20210923T143258', 'value4-7']
        ! @ [5]
          L 8 ['1003', 'value1-e', 'key2-4', '1008', '20210923T143259', 'value4-8']
          R 7 ['1003', 'value1-8', 'key2-4', '1008', '20210923T143257', 'value4-e']
        
        ● Count & Row number
        same lines           : 3
        left side only    (<): 2 :-- Row Numbers      -->: [5, 7]
        right side only   (>): 1 :-- Row Numbers      -->: [2]
        with differences  (!): 2 :-- Row Number Pairs -->: [(4, 5), (8, 7)]
    ''')



