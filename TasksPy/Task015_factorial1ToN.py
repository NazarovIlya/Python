# Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num = int(input('Введите любое целое число: '))

def find_product(number):
    factorial = 1
    list = []
    for n in range(1, number + 1):
        factorial *= n
        list.append(factorial)
    return list
result = find_product(num)
print(f'Факториалом числел от 1 до {num} являются ', end= '' )
print(result, end= '')