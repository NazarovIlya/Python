# Для натурального n создать список, состоящий из элементов последовательности 3n + 1
# Пример:
# - Для n = 6: [4, 7, 10, 13, 16, 19]

def sequence_num(number):
    list = []
    list.append(1)
    for n in range(1, number + 1):
        list.append(3 * n + 1)
    return list

num = int(input("Введите любое натуральное число n: "))
result = sequence_num(num)
print(*result, sep= ', ')