# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.

# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def input_list():
    user_list = input('Введите несколько вещественных чисел через пробел: ').split(' ')
    return user_list


def find_difference(user_list, signs):
    current_value = 0.0
    min_value = float(user_list[0]) % 1
    max_value = float(user_list[0]) % 1
    error_correction = 0.0000000000000001
    for i in user_list:
        current_value = float(i) % 1
        if current_value != 0:
            if current_value > max_value:
                max_value = current_value
            elif current_value < min_value:
                min_value = current_value
        difference = max_value - min_value + error_correction
        difference = round(difference, 14)
    return difference


user_lst = input_list()
signs = int(input('Сколько знаков после запятой Вы хотите видеть в результирующей?: '))
result = find_difference(user_lst, signs)
print(result)