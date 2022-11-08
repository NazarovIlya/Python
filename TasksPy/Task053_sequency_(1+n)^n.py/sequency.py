# Написать функцию-декоратор для кеширования значений функции
# Написать функцию seq(n)
# n = 0 ....N
# (1 + n) ** n возвращает [x1, x2, x3, , , , xn]
# 1.1 (**) с помощью декоратора-логгера создать лог функции (с замером времени выполнения функции)


def cacher(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = args
        if key not in cache:
            cache[key] = func(*args, kwargs)
        print(cache)
        return cache
    return wrapper

