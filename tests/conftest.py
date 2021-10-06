import os

import pytest

from src.csvdiff3.csvdiff import MatchingKeyInfo


@pytest.fixture(scope='function')
def args():
    return type("Arguments", (object,), {
        "lhs_file_name": "",
        "rhs_file_name": "",
        "encoding": "",
        "encoding_for_lhs": "utf8",
        "encoding_for_rhs": "utf8",
        "matching_keys": [MatchingKeyInfo('0')],
        "unique_key": False,
        "ignore_columns": [],
        "vertical_style": False,
        "show_count": False,
        "show_difference_only": False,
        "show_all_lines": False,
        "show_context_from_arguments": False,
        "sniffing_size": 4096,
        "force_individual_specs": False,
        "header": None,
        "column_separator": None,
        "line_separator": None,
        "quote_char": None,
        "no_skip_space_after_column_separator": "",
        "column_separator_for_lhs": "COMMA",
        "column_separator_for_rhs": "COMMA",
        "line_separator_for_lhs": "LF",
        "line_separator_for_rhs": "LF",
        "quote_char_for_lhs": '"',
        "quote_char_for_rhs": '"',
        "no_skip_space_after_column_separator_for_lhs": False,
        "no_skip_space_after_column_separator_for_rhs": False,
    })

@pytest.fixture(scope='function')
def lhs(tmpdir):
    lhs = tmpdir.join("left.csv")
    return lhs

@pytest.fixture(scope='function')
def rhs(tmpdir):
    rhs = tmpdir.join("right.csv")
    return rhs

@pytest.fixture(scope='function')
def path_to_tests_dir():
    return './' if current_folder_name() == 'tests' else 'tests'

def current_folder_name():
    return os.path.basename(os.getcwd())

@pytest.fixture(scope='function')
def lhs_dir(tmpdir):
    lhs = tmpdir.mkdir("left_dir")
    return lhs

@pytest.fixture(scope='function')
def rhs_dir(tmpdir):
    rhs = tmpdir.mkdir("right_dir")
    return rhs


