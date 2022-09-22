# Показать первую цифру дробной части числа.

number = int(input('Введите целое число: '))
while number > 10:
    number //= 10
    
print(number)