# Напишите программу, удаляющую из текста все слова, содержащие "абв".


def input_marker():
    user_list = input('Введите сочетание букв для определения удаляемых слов(строк): ').split(' ')
    if len(user_list) == 1:
        return user_list
    else:
        quit('Введите корректные данные.')


def input_list():
    user_list = input('Введите некоторое количество слов через пробел: ').split(' ')
    if len(user_list) > 1:
        return user_list
    else:
        quit('Введите корректные данные.')
        


marker_lst = input_marker()
input_lst = input_list()
user_lst = list(filter(lambda x: not marker_lst[0] in x, input_lst))
print('Маркер, по которому слова будут/строки будут удаляться: ', end= '')
print(*marker_lst)
print('Исходная последовательность: ', end= '')
print(*input_lst)
print('Обработаннная последовательность: ', sep= ',')
print(*user_lst)
