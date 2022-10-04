# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0


import random


def write_to_file_ratois(degree):
    a = random.randint(0, 101)
    b = random.randint(0, 101)
    c = random.randint(0, 101)
    with open('multiple_task034', 'w') as f:
        f.write(f'{a}x^{degree} + {b}x + {c}')
    

num = int(input('Введите натуральную степнь k: '))
write_to_file_ratois(num)