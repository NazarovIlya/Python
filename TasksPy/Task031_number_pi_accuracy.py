# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141 10^-1 <= d <= 10^-10


import math


def get_count_sings(number):
    signs = 0
    if 0.1 >= number >= 0.0000000001:
        while number < 1:
            number *= 10
            signs += 1
        pi = math.pi
        return round(pi, signs)
    else:
        print('Введите корретные данные в диапазоне от 10^-1 до 10*^-10: ')
        quit()
        

num = float(input('Введите точность числа, которую хотели бы получить форматом, например 0.001: '))        
print(get_count_sings(num))