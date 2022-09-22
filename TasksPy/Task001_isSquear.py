# По двум заданным числам проверить является ли одно квадратом второго.

firstNumber = int(input('Введите целое число: '))
secondNumber = int(input('Введите целое число: '))
if firstNumber / secondNumber == secondNumber:
    print(f'Число {firstNumber}(первое) являетя квадратом числа {secondNumber}(второго)')
elif secondNumber / firstNumber == firstNumber:
    print(f'Число {secondNumber}(второе) являетя квадратом числа {firstNumber}(первого)')
else:
    print(f'Ни одно число не является квадратом другого')