# Реализовать алгоритм перемешивания списка.

import random

def new_list(number):
    list = []
    for n in range(0, number):
        list.append(random.randint(-100, 100))
    return list

def mix(list):
    for i in range(0, len(list)):
        random_index = random.randint(0, len(list) - 1)
        temp = list[i]
        list[i] = list[random_index]
        list[random_index] = temp
    return list

num = int(input('Введите количество элементов списка: '))
original_list = new_list(num) 
print(f'Исходный список: {original_list}')
mixed_list = mix(original_list)
print(f'Перемешанный список: {mixed_list}')