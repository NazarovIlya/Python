# Показать первую цифру дробной части числа.

number = float(input('Введите дробное число: '))
round_num = int(number)
result = (number - round_num)*10
print(f'Первая цифра дробного числа: {int(result)}')