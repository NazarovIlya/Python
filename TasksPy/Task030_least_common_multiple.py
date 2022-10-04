# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее
# кратное) этих двух чисел.


def input_list():
    user_list = input('Введите два числа через пробел: ').split(' ')
    return user_list


def least_common_multiple(user_list):
    if len(user_list) == 2:
        first_value = int(user_list[0])
        second_value = int(user_list[1])
        multiple = first_value * second_value
        multiple = first_value * second_value
        if multiple / first_value == 0 and multiple / second_value == 0:
            return multiple
    else:
        return -1
    
    
number_list = input_list()
result = least_common_multiple(number_list)
print(result)