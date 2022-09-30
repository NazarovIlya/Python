# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def input_list():
    user_list = input('Введите несколько чисел через пробел: ').split(' ')
    return user_list


def sum_list_elements(user_list):
    current_sum = 0
    for i in user_list:
        if user_list.index(i) % 2 != 0:
            current_sum += int(i)
    return current_sum


user_lst = input_list()
print(user_lst)
result = sum_list_elements(user_lst)
print(f'Сумма элементов стоящих на нечетных позициях состовляет {result}')
