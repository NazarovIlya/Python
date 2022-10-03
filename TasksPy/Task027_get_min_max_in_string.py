# Задайте строку из набора чисел. Напишите программу, которая покажет большее и
# меньшее число. В качестве символа-разделителя используйте пробел.


def input_list():
    user_list = input('Введите несколько вещественных чисел через пробел: ').split(' ')
    return user_list


def get_min_max(user_string):
    min_value = user_string[0]
    max_value = user_string[0]
    for current_value in user_string:
        if int(current_value) < int(min_value):
            min_value = current_value
        elif int(current_value) > int(max_value):
            max_value = current_value
    return min_value, max_value


numbers_list = input_list()
print(*numbers_list)
result = get_min_max(numbers_list)
print(f'Минимальное найденное значение = {result[0]}, максимальное найденное значение = {result[1]}')