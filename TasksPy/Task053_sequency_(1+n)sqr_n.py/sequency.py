# Написать функцию-декоратор для кеширования значений функции
# Написать функцию seq(n)
# n = 0 ....N
# (1 + n) ** n возвращает [x1, x2, x3, , , , xn]
# 1.1 (**) с помощью декоратора-логгера создать лог функции (с замером времени выполнения функции)

from functools import wraps


def cacher(func):
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        key = args
        if key not in cache:
            cache[key] = func(*args)
        print(cache)
        return cache[key]
    return wrapper


@cacher
def sequency(number):
    # (1 + n) ** n
    result = 0
    for i in range(number):
        result = (1 + number) ** number
    return result


def main():
    print(sequency(5))
    print(sequency(8))
    print(sequency(12))
    print(sequency(16))
    
    
if __name__ == '__main__':
    main()