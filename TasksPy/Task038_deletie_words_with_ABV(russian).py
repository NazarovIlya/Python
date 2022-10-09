# Напишите программу, удаляющую из текста все слова, содержащие "абв".


def input_list():
    user_list = input('Введите два числа через пробел: ').split(' ')
    if len(user_list) == 2:
        return user_list
    else:
        quit('Введите корректные данные.')
        
        
        
        
marker_string = 'абв' # input('Введите сочетание букв для определения удаляемых слов(строк): ')
input_lst = input_list()
