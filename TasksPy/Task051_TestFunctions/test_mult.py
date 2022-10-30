import pytest
from task_functions import mult


@pytest.mark.parametrize("a, b, excepted", [(3, 3, 9),
                                            (5, 5, 25),
                                            (4, 4, 16),
                                            (-1, 5, -5),
                                            (8, 0, 0)])

def test_mult(a, b, excepted):
    assert mult(a, b) == excepted