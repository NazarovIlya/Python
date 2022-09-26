# Напишите программу, которая принимает на вход число N и выдаёт 
# последовательность из N членов.
# Пример:
# - Для N = 5: 1, -3, 9, -27, 81

def sequence_num(number):
    list = []
    list.append(1)
    for i in range(1, number - 1):
        list.append(list[i - 1] * (-3))
    return list

num = int(input("Введите любое натуральное число n: "))
result = sequence_num(num)
print(*result, sep= ', ')