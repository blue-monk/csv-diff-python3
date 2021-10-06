import os.path
import sys
import textwrap

from src.csvdiff3 import csvdiff


TEST_DATA_DIR = 'data/e2e_04_special_char'

def test_special_character_in_value(path_to_tests_dir, capfd):
    """ special character: line-break, comma, tab, single-quotation, double-quotation, semicolon """

    lhs_csv = os.path.join(path_to_tests_dir, TEST_DATA_DIR, 'left.csv')
    rhs_csv = os.path.join(path_to_tests_dir, TEST_DATA_DIR, 'right.csv')

    sys.argv = ['csvdiff.py', lhs_csv, rhs_csv, '-k0:4,2', '-ac', '-i1,4']
    csvdiff.main()

    out, err = capfd.readouterr()
    assert err == ''
    assert out == textwrap.dedent('''
        ============ Report ============
        
        ● All
        ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        left.csv                                                                                    right.csv                                                                                  Column indices with difference
        ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                 >  2 ['1', 'value1-1', 'key2-1', '1001', '20210921T035901', 'value4-1']                   
        2 ['1', 'value1 and \\nvalue-2', 'key2-2', '1,002', '20210921;035902', "value'4'tab\\t2"]     3 ['1', 'value1 and \\nvalue-2', 'key2-2', '1,002', '20210921;035902', "value'4'tab\\t2"]
        3 ['1', 'value1-3', 'key2-3', '1003', '20210921\\nT035904', 'value"4"\\n-3']               !  4 ['1', 'value1-3', 'key2-3', '1003', '20210921\\nT035904', 'value"4"-\\n3']               @ [5]
        4 ['102', 'value1-4', 'key2-1', '1004', '20210924T180521', 'value4-e']                   !  5 ['102', 'value1-4e', 'key2-1', '1044', '20210924T180529', 'value4-4']                  @ [3, 5]
        5 ['1003', 'value1-5', 'key2-1', '1005', '20210924T180528', 'value4-5']                  <  
        6 ['1003', 'value1 and\\nvalue-6', 'key2-2', '1,006', '20210923T143259', 'value4tab\\t6']  !  6 ['1003', 'value1 and\\nvalue6', 'key2-2', '1006', '20210923;143259', 'value4\\t6']       @ [3, 5]
        7 ['1003', 'value1-7', 'key2-3', '1007', '20210923T143258', 'value4-7']                  <  
        8 ['1003', 'value1-e', 'key2-4', '1008', '20210923T143259', 'value4-8']                  !  7 ['1003', 'value1-8', 'key2-4', '1008', '20210923T143257', 'value4-e']                  @ [5]
        
        ● Count & Row number
        same lines           : 1
        left side only    (<): 2 :-- Row Numbers      -->: [5, 7]
        right side only   (>): 1 :-- Row Numbers      -->: [2]
        with differences  (!): 4 :-- Row Number Pairs -->: [(3, 4), (4, 5), (6, 6), (8, 7)]
    ''')



