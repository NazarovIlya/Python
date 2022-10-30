import pytest
from task_functions import sequence_minusN_to_N


@pytest.mark.parametrize('number, excepted', [(1, [-1, 0, 1]),
                                              (3, [-3, -2, -1, 0, 1, 2, 3]),
                                              (5, [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]),
                                              (-5, [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]),
                                              (0, [0])])
def test_sequence(number, excepted):
    assert sequence_minusN_to_N(number) == excepted