# Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

def input_list():
    string = input('Введите значения строк через пробел: ').split(' ')
    return string

def find_number(string, number):
        for item in string:
            if number in item:
                print(f'В элементе {item} списка найдено число {number}')
        print(f'Список изучен')  
        return


string_list = input_list()
num = input('Введите число, которое необходимо найти  списке: ')
print(string_list)
find_number(string_list, num)
