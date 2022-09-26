# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num_list = input('Введите число: ')

def find_sum_digits(list): 
    list = list.replace(".", "", 1)
    sum = 0
    for i in range(len(list)):
        sum += int(list[i])
    return sum
    
print(f'Сумма всех цифр в числе {num_list} равна {find_sum_digits(num_list)}')