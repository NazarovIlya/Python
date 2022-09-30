# Реализуйте алгоритм задания случайных чисел без использования 
# встроенного генератора псевдослучайных чисел.

import time

def random_number(count_digits):
    order = 10
    for i in range(1, count_digits):
        order *= 10
    rnd_number = 0
    order_length = order / 10
    while(rnd_number < order_length):
        random_number = time.time_ns() // 1000
        rnd_number = random_number
        rnd_number %= order
    return rnd_number


while(1):
    order = int(input('Задайте порядок случайного числа: '))
    rnd = random_number(order)
    print(rnd)