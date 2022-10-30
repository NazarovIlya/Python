import pytest
from task_functions import get_max


@pytest.mark.parametrize('input_list, excepted', [([3, 5, -9, 23, 2], 23),
                                                  ([64, -345, 3145, 55, -543, 3, 6452, -315], 6452),
                                                  ([555, 56, -13, 13, -134, 14, 5, 123], 555),
                                                  ([342,65, -67, 3, 243, 53, -453, 341, -77], 342)])
def test_get_max_good(input_list, excepted):
    assert get_max(input_list) == excepted