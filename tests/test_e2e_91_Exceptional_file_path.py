import sys
import textwrap

import pytest

from src.csvdiff3 import csvdiff


def test_misspecification_of_csv_file_path_on_the_left(lhs, rhs, capfd):

    lhs.write(textwrap.dedent('''
        head1, head2, head3, head4
        key1-1, value1-1, value2-1, value3-1
        key1-2, value1-2, value2-2, value3-2
    ''').strip())
    rhs.write(textwrap.dedent('''
        head1, head2, head3, head4
        key1-1, value1-1, value2-1, value3-1
        key1-2, value1-2, value2-2, value3-2
    ''').strip())

    sys.argv = ['csvdiff.py', 'not_exists' + lhs.strpath, rhs.strpath, '-d']
    with pytest.raises(SystemExit) as e:
        csvdiff.main()

    assert e.type == SystemExit
    assert e.value.code == 1

    _, err = capfd.readouterr()
    assert str(err).find("lhs_file_path not exists. ") > 0

def test_misspecification_of_csv_file_path_on_the_right(lhs, rhs, capfd):

    lhs.write(textwrap.dedent('''
        head1, head2, head3, head4
        key1-1, value1-1, value2-1, value3-1
        key1-2, value1-2, value2-2, value3-2
    ''').strip())
    rhs.write(textwrap.dedent('''
        head1, head2, head3, head4
        key1-1, value1-1, value2-1, value3-1
        key1-2, value1-2, value2-2, value3-2
    ''').strip())

    sys.argv = ['csvdiff.py', lhs.strpath, 'not_exists' + rhs.strpath, '-d']
    with pytest.raises(SystemExit) as e:
        csvdiff.main()

    assert e.type == SystemExit
    assert e.value.code == 1

    _, err = capfd.readouterr()
    assert str(err).find("rhs_file_path not exists. ") > 0

def test_specified_left_csv_file_path_is_directory(lhs, rhs, lhs_dir, capfd):

    lhs.write(textwrap.dedent('''
        head1, head2, head3, head4
        key1-1, value1-1, value2-1, value3-1
        key1-2, value1-2, value2-2, value3-2
    ''').strip())
    rhs.write(textwrap.dedent('''
        head1, head2, head3, head4
        key1-1, value1-1, value2-1, value3-1
        key1-2, value1-2, value2-2, value3-2
    ''').strip())

    sys.argv = ['csvdiff.py', lhs_dir.strpath, rhs.strpath, '-d']
    with pytest.raises(SystemExit) as e:
        csvdiff.main()

    assert e.type == SystemExit
    assert e.value.code == 1

    _, err = capfd.readouterr()
    assert str(err).find("lhs_file_path is not a file.") > 0

def test_specified_right_csv_file_path_is_directory(lhs, rhs, rhs_dir, capfd):

    lhs.write(textwrap.dedent('''
        head1, head2, head3, head4
        key1-1, value1-1, value2-1, value3-1
        key1-2, value1-2, value2-2, value3-2
    ''').strip())
    rhs.write(textwrap.dedent('''
        head1, head2, head3, head4
        key1-1, value1-1, value2-1, value3-1
        key1-2, value1-2, value2-2, value3-2
    ''').strip())

    sys.argv = ['csvdiff.py', lhs.strpath, rhs_dir.strpath, '-d']
    with pytest.raises(SystemExit) as e:
        csvdiff.main()

    assert e.type == SystemExit
    assert e.value.code == 1

    _, err = capfd.readouterr()
    assert str(err).find("rhs_file_path is not a file.") > 0



