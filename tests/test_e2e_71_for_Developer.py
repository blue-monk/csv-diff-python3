import sys
import textwrap

from src.csvdiff3 import csvdiff


def test_option_x_1(lhs, rhs, capfd):

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

    sys.argv = ['csvdiff.py', lhs.strpath, rhs.strpath, '-x']
    csvdiff.main()

    out, err = capfd.readouterr()
    assert err == ''
    assert out == textwrap.dedent('''
        ============ Report ============

        ● Context
        File Path on the Left-Hand Side: {lhs_file_path}
        File Path on the Right-Hand Side : {rhs_file_path}
        Matching Key Indices: [MatchingKeyInfo(0, '<not specified>')]
        Matching Key Is Unique?: False
        Column Indices to Ignore: []
        with Header?: True
        Report Style: Two facing (Horizontal)
        Show Count?: True
        Show Difference Only?: False
        Show All?: False
        Show Context?: True
        File Encoding for Left-Hand Side: utf8
        File Encoding for Right-Hand Side: utf8
        CSV Sniffing Size: 4096
        --- csv analysis conditions ---
        Forces Individual Specified Conditions?: False
        column_separator_for_lhs: COMMA
        column_separator_for_rhs: COMMA
        line_separator_for_lhs: 0d0a
        line_separator_for_rhs: 0d0a
        quote_char_for_lhs: "
        quote_char_for_rhs: "
        skips_space_after_column_separator_for_lhs: True
        skips_space_after_column_separator_for_rhs: True
        
        ● Count & Row number
        same lines           : 0
        left side only    (<): 2 :-- Row Numbers      -->: [7, 8]
        right side only   (>): 1 :-- Row Numbers      -->: [4]
        with differences  (!): 5 :-- Row Number Pairs -->: [(2, 2), (3, 3), (4, 5), (5, 6), (6, 7)]
    ''').format(lhs_file_path=lhs.strpath, rhs_file_path=rhs.strpath)


def test_option_x_2(lhs, rhs, capfd):

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

    sys.argv = ['csvdiff.py', lhs.strpath, rhs.strpath, '-k0:4,2', '-avx']
    csvdiff.main()

    out, err = capfd.readouterr()
    assert err == ''
    assert out == textwrap.dedent('''
        ============ Report ============

        ● Context
        File Path on the Left-Hand Side: {lhs_file_path}
        File Path on the Right-Hand Side : {rhs_file_path}
        Matching Key Indices: [MatchingKeyInfo(0, 4), MatchingKeyInfo(2, '<not specified>')]
        Matching Key Is Unique?: False
        Column Indices to Ignore: []
        with Header?: True
        Report Style: Vertical
        Show Count?: False
        Show Difference Only?: False
        Show All?: True
        Show Context?: True
        File Encoding for Left-Hand Side: utf8
        File Encoding for Right-Hand Side: utf8
        CSV Sniffing Size: 4096
        --- csv analysis conditions ---
        Forces Individual Specified Conditions?: False
        column_separator_for_lhs: COMMA
        column_separator_for_rhs: COMMA
        line_separator_for_lhs: 0d0a
        line_separator_for_rhs: 0d0a
        quote_char_for_lhs: "
        quote_char_for_rhs: "
        skips_space_after_column_separator_for_lhs: True
        skips_space_after_column_separator_for_rhs: True
        
        ● All
        --------------------------------------------------------------------------------
        L left.csv
        R right.csv
        --------------------------------------------------------------------------------
        > R 2 ['0001', 'value1-1', 'key2-1', '1001', '20210921T035901', 'value4-1']
        =
          L 2 ['0001', 'value1-2', 'key2-2', '1002', '20210921T035902', 'value4-2']
          R 3 ['0001', 'value1-2', 'key2-2', '1002', '20210921T035902', 'value4-2']
        ! @ [4]
          L 3 ['0001', 'value1-3', 'key2-3', '1003', '20210921T035904', 'value4-3']
          R 4 ['0001', 'value1-3', 'key2-3', '1003', '20210921T035903', 'value4-3']
        ! @ [1, 3, 4, 5]
          L 4 ['0102', 'value1-4', 'key2-1', '1004', '20210924T180521', 'value4-e']
          R 5 ['0102', 'value1-4e', 'key2-1', '1044', '20210924T180529', 'value4-4']
        < L 5 ['1003', 'value1-5', 'key2-1', '1005', '20210924T180528', 'value4-5']
        =
          L 6 ['1003', 'value1-6', 'key2-2', '1006', '20210923T143259', 'value4-6']
          R 6 ['1003', 'value1-6', 'key2-2', '1006', '20210923T143259', 'value4-6']
        < L 7 ['1003', 'value1-7', 'key2-3', '1007', '20210923T143258', 'value4-7']
        ! @ [1, 4, 5]
          L 8 ['1003', 'value1-e', 'key2-4', '1008', '20210923T143259', 'value4-8']
          R 7 ['1003', 'value1-8', 'key2-4', '1008', '20210923T143257', 'value4-e']

    ''').format(lhs_file_path=lhs.strpath, rhs_file_path=rhs.strpath)



