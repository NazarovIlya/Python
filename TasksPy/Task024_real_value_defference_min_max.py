# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.

# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def input_list():
    user_list = input('Введите несколько вещественных чисел через пробел: ').split(' ')
    return user_list


def find_difference(user_list, signs):
    temp = 0.0
    min_value = float(user_list[0]) % 1
    max_value = float(user_list[0]) % 1
    error_correction = 0.0000000000000001
    for i in user_list:
        temp = float(i) % 1
        if temp != 0:
            if temp > max_value:
                max_value = temp
            elif temp < min_value:
                min_value = temp
        difference = max_value - min_value + error_correction
        difference = round(difference, 14)
    return difference


user_lst = input_list()
signs = int(input('Сколько знаков после запятой Вы хотите видеть в результирующей?: '))
result = find_difference(user_lst, signs)
print(result)