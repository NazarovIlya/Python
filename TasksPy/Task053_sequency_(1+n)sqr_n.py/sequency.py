# Написать функцию-декоратор для кеширования значений функции
# Написать функцию seq(n)
# n = 0 ....N
# (1 + n) ** n возвращает [x1, x2, x3, , , , xn]
# 1.1 (**) с помощью декоратора-логгера создать лог функции (с замером времени выполнения функции)

from decorators import *
            

@logger
@cacher
def result_of_sequency(number):
    # (1 + n) ** n
    result = 0
    for i in range(number):
        result = (1 + number) ** number
    return result


@logger
@cacher
def sequency(number):
    # (1 + n) ** n
    result = 0
    lst = []
    for i in range(number):
        result = (1 + i) ** i
        lst.append(result)
    return lst


def main():
    print(sequency(1))
    print(sequency(3))
    print(sequency(5))
    print(sequency(8))
    print(result_of_sequency(4))
    print(result_of_sequency(8))
    print(result_of_sequency(12))
    print(result_of_sequency(16))
    
    
if __name__ == '__main__':
    main()