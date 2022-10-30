import pytest
from task_functions import is_square
    
result_1 = f'Число {16}(первое) являетя квадратом числа {4}(второго)'
result_2 = f'Число {16}(второе) являетя квадратом числа {4}(первого)'
result_3 = f'Ни одно число не является квадратом другого'
@pytest.mark.parametrize('a, b, excepted', [(16, 4, result_1),
                                            (4, 16, result_2),
                                            (5, 5, result_3)])
def test_is_squere_good(a, b, excepted):
    assert is_square(a, b) == excepted
     