import pytest
from task_functions import get_first_float_digit


@pytest.mark.parametrize('number, excepted', [(2.35, 3),
                                              (5.25, 2),
                                              (7.89, 8),
                                              (1.05, 0),
                                              (9.75, 7),
                                              (-7.76, 7),
                                              (-8.95, 9),
                                              (-6.43, 4)])
def test_get_first_float_digit(number, excepted):
    assert get_first_float_digit(number) == excepted