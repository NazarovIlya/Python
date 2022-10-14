# Для натурального n создать список, состоящий из элементов последовательности 3n + 1
# Пример:
# - Для n = 6: [4, 7, 10, 13, 16, 19]
#! Модификация Task012

def sequence_num(number):
    lst = [i for i in range(1, number)]
    lst = list(map(lambda x: 3*x + 1, lst))
    return lst

num = int(input("Введите любое натуральное число n: "))
result = sequence_num(num)
print(*result, sep= ', ')