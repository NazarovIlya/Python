# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
#! Модификация Task033


def input_list():
    user_list = input('Введите несколько вещественных чисел через пробел: ').split(' ')
    return user_list


def unique_numbers_sequence(user_list):
    return list(filter(lambda x: user_list.count(x) == 1, user_list))
    

input_list = input_list()
result = unique_numbers_sequence(input_list)
print(f'В исходной последовательности: {input_list} неповторяющимися являются чила: {result}')