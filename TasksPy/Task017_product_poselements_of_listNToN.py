#Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов
# на указанных позициях. Позиции хранятся в списке positions - создайте этот список (например:
# positions = [1, 3, 6]).

def input_positions(number):
    list = []
    count_pos = int(input(f'Сколько элементов списка из {number * 2} Вы хотели бы перемножить?: '))
    for n in range(count_pos):
        position = int(input(f'Введите значение для элемента {n + 1} от 1 до {(number * 2) + 1}: '))
        position -= 1
        list.append(position)
    return list

def sequence(number):
    list = []
    if number > 0:
        number *= (-1)
    for n in range(number, number * (-1) + 1):
        list.append(n)
    return list

def sequence_for_product(list, positions):
    list_product = []
    for n in range(len(positions)):
        list_product.append(list[positions[n]])
    return list_product

def product(list, positions):
    product = 1
    for n in range(len(positions)):
        product *= list[positions[n]]
    return product
    
num_n = int(input('Введите количество элементов: '))
pos_list = input_positions(num_n)
num_list = sequence(num_n)
product_sequence = sequence_for_product(num_list, pos_list)
result = product(num_list, pos_list)
print(*num_list, sep= ', ')
print(*product_sequence, sep= ' * ', end= '')
print(f' = {result}')