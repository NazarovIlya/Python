# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.


def input_list():
    user_list = input('Введите несколько вещественных чисел через пробел: ').split(' ')
    return user_list


def unique_numbers_sequence(user_list):
    new_list = []
    for i in user_list:
        count = user_list.count(i)
        if count == 1:
            new_list.append(i)
    return new_list
    

input_list = input_list()
result = unique_numbers_sequence(input_list)
print(f'В исходной последовательности: {input_list} неповторяющимися являются чила: {result}')