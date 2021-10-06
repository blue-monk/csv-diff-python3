import pytest

from src.csvdiff3.csvdiff import ValueDifferenceDetector


class Condition:

    def __init__(self, cols, keys, ignores, lhs, rhs):
        self.cols = cols
        self.keys = keys
        self.ignores = ignores
        self.lhs = lhs
        self.rhs = rhs

class Expected:

    def __init__(self, has_difference, different_column_indices):
        self.has_difference = has_difference
        self.different_column_indices = different_column_indices


@pytest.mark.parametrize(
    "condition, expected",
    [
        pytest.param(Condition(cols=5, keys=[0], ignores=[],
                               lhs=['1', 'value-1', 'value-2', 'value-3', 'value-4'],
                               rhs=['1', 'value-1', 'value-2', 'value-3', 'value-4']),     Expected(has_difference=False, different_column_indices=[]),          id='no difference : 1 numerical key'),
        pytest.param(Condition(cols=5, keys=[4], ignores=[],
                               lhs=['value-1', 'value-2', 'value-3', 'value-4', 'key-1'],
                               rhs=['value-1', 'value-2', 'value-3', 'value-4', 'key-1']), Expected(has_difference=False, different_column_indices=[]),          id='no difference : 1 alphabetical key'),
        pytest.param(Condition(cols=5, keys=[0, 3], ignores=[],
                               lhs=['key-1', 'value-1', 'value-2', '7', 'value-3'],
                               rhs=['key-1', 'value-1', 'value-2', '7', 'value-3']),       Expected(has_difference=False, different_column_indices=[]),          id='no difference : multiple keys'),
        pytest.param(Condition(cols=5, keys=[4, 0], ignores=[],
                               lhs=['key-1', 'value-1', 'value-2', 'value-3', '7'],
                               rhs=['key-1', 'value-1', 'value-2', 'value-3', '7']),       Expected(has_difference=False, different_column_indices=[]),          id='no difference : multiple keys in reverse order'),
        pytest.param(Condition(cols=5, keys=[1], ignores=[],
                               lhs=['value-1', '1', 'value-2', 'value-3', 'value-4'],
                               rhs=['value-2', '1', 'value-2', 'value-3', 'value-4']),     Expected(has_difference=True, different_column_indices=[0]),          id='1 difference : at first'),
        pytest.param(Condition(cols=5, keys=[1], ignores=[],
                               lhs=['value-1', '1', 'value-2', 'value-3', 'value-5'],
                               rhs=['value-1', '1', 'value-2', 'value-3', 'value-4']),     Expected(has_difference=True, different_column_indices=[4]),          id='1 difference : at last'),
        pytest.param(Condition(cols=5, keys=[1], ignores=[],
                               lhs=['value-1', '1', 'value-2', 'value-3', 'value-5'],
                               rhs=['value-0', '1', 'value-3', 'value-2', 'value-4']),     Expected(has_difference=True, different_column_indices=[0, 2, 3, 4]), id='multi differences : all columns'),
        pytest.param(Condition(cols=5, keys=[1], ignores=[0],
                               lhs=['value-1', '1', 'value-2', 'value-3', 'value-5'],
                               rhs=['value-0', '1', 'value-3', 'value-2', 'value-4']),     Expected(has_difference=True, different_column_indices=[2, 3, 4]),    id='multi differences : with first column ignored'),
        pytest.param(Condition(cols=5, keys=[1], ignores=[4],
                               lhs=['value-1', '1', 'value-2', 'value-3', 'value-5'],
                               rhs=['value-0', '1', 'value-3', 'value-2', 'value-4']),     Expected(has_difference=True, different_column_indices=[0, 2, 3]),    id='multi differences : with last column ignored'),
        pytest.param(Condition(cols=5, keys=[1], ignores=[2, 4],
                               lhs=['value-1', '1', 'value-2', 'value-3', 'value-5'],
                               rhs=['value-0', '1', 'value-3', 'value-2', 'value-4']),     Expected(has_difference=True, different_column_indices=[0, 3]),       id='multi differences : with multi columns ignored'),
    ],
)
def test_value_difference_detector(condition, expected):

    sut = ValueDifferenceDetector(number_of_columns=condition.cols , matching_key_indices=condition.keys, ignore_column_indices=condition.ignores)

    actual = sut.detect_difference_between(condition.lhs, condition.rhs)

    assert actual.has_difference == expected.has_difference
    assert actual.different_column_indices == expected.different_column_indices



