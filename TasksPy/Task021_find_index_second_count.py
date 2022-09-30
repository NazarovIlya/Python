# Напишите программу, которая определит позицию второго вхождения 
# строки в списке либо сообщит, что её нет.
# Пример:
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1


def input_list():
    string = input('Введите некоторый текст: ').split(' ')
    return string


def get_index(user_list, user_element):
    count = user_list.count(user_element)
    if count > 1:
        position = user_list.index(user_element)
        position = user_list.index(user_element, position + 1)
    else:
        position = -1
    return position


def output_result(result, user_element):
    if result != -1:
        print(f'Второе вхождение искомого элемента {user_element} имеет индекс {result}')
    else:
        print(f'{-1}, второе вхождение значения "{user_element}"  списке не найдено.')


user_lst = input_list()
user_str = input('Введите значение искомое строки: ')
print(f'Задан список: {user_lst}')
result = get_index(user_lst, user_str)
output_result(result, user_str)
