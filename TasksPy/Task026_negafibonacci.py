# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def nega_fibofibonacci(number):
    fibo = 0
    fibo_1 = 1
    fibo_2 = 1
    negafibo = 0
    negafibo_1 = 1
    negafibo_2 = -1
    fibo_list = [0, 1, 1]
    negafibo_list_temp = [1, -1]
    negafibo_list = []
    for i in range(2, number):
        fibo = fibo_1 + fibo_2
        fibo_list.append(fibo)
        fibo_1 = fibo_2
        fibo_2 = fibo
    for i in range(2, number):
        negafibo = negafibo_1 - negafibo_2
        negafibo_1 = negafibo_2
        negafibo_2 = negafibo
        negafibo_list_temp.append(negafibo)
    for i in range(len(negafibo_list_temp)):
        fibo_temp = negafibo_list_temp.pop()
        negafibo_list.append(fibo_temp)
    negafibo_list.extend(fibo_list)
    return negafibo_list


num = int(input('Введите номер крайнего числа негафибоначчи: '))
result = nega_fibofibonacci(num)
print(f'Последовательность чисел негафибоначчи для n = {num}:')
print(*result, sep= ', ')
