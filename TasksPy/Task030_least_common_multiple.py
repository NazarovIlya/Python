# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее
# кратное) этих двух чисел.


def input_list():
    user_list = input('Введите два числа через пробел: ').split(' ')
    if len(user_list) == 2:
        return user_list
    else:
        print('Введите корректные данные.')


def nod(a, b):
    if b == 0:
        return a
    else:
        return nod(b, a % b)


def nok(a, b):
    return int(abs(a * b) / nod(a, b))

   
user_str = input_list()
num_a = int(user_str[0])
num_b = int(user_str[1])
result = nok(num_a, num_b)
print(f'Наименьшим общим кратным для {num_a} и {num_b} является {result}')