# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


def input_list():
    user_list = input('Введите несколько чисел через пробел: ').split(' ')
    return user_list

def find_product(user_list):
    result_list = []
    product = 1
    if len(user_list) / 2 == 0:
        for i in range(int((len(user_list) / 2))):
            product = int(user_list[i]) * int(user_list[len(user_list) - 1 - i])
            result_list.append(product)
    else:
        for i in range(int((len(user_list) / 2))):
            product = int(user_list[i]) * int(user_list[len(user_list) - 1 - i])
            result_list.append(product)
        product = int(user_list[int((len(user_list) / 2))]) ** 2
        result_list.append(product)
    return result_list


user_lst = input_list()
print(user_lst)
result = find_product(user_lst)
print(result)