# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не
# хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.


import random


def get_sequence(number):
    str_sequence = []
    i = 0
    current = random.randint(number, number ** 2)
    while i < number:
        str_sequence.append(current)
        current += 1
        i += 1
    print(f'Сформирована сделующая полседовательность: ',end= '')
    print(*str_sequence)     # Вывод происходит здесь, так как на следующем этапе последовательность теряет один из элементов77
    random_index = random.randint(1, len(str_sequence) - 2)     # оставляем первый и последний
    str_sequence.pop(random_index)      # элементы списка, чтобы не удалять их значения
    return str_sequence


def write_sequence_to_file(input_sequence, file_path):
    with open(file_path, 'w') as new_file:
        input_sequence_str = str(input_sequence)
        for i in range(1, len(input_sequence_str) - 1):
            new_file.write(input_sequence_str[i])


def read_list_from_file(file_path):
    with open(file_path, 'r') as str_file:
        input_list = []
        input_string = str_file.read().replace(',', '')
        input_list = input_string.split()
    return input_list
        
        
def find_delete_element(input_sequence):
    for i in range(1, len(input_sequence)):
        if int(input_sequence[i]) - 1 != int(input_sequence[i - 1]):
            return int(input_sequence[i]) - 1


 
 
num = int(input('Введите количество элементов списка: '))
path_input_file = "./task036/input_data.txt"
sequence = get_sequence(num)
write_sequence_to_file(sequence, path_input_file)
sequence_from_file = read_list_from_file(path_input_file)
print('Последовательность с удаленным элементом: ', end= '')
print(*sequence_from_file)
result = find_delete_element(sequence_from_file)
print('Найден недостающий элемент последовательности: ', end= '')
print(result)
