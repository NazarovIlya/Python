import os
os.system('cls')
firstNumber = int(input('Введите первое число: '))
secondNumber = int(input('Введите второе число: '))
firstNumber / secondNumber
if (firstNumber / secondNumber) == secondNumber:
    print(f'Число {firstNumber} является квадратом числа {secondNumber}')
elif (secondNumber / firstNumber) == firstNumber:
    print(f'Число {secondNumber} является квадратом числа {firstNumber}')
else:
    print('Ни одно число не является квадратом другого.')