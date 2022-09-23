# По двум заданным числам проверить является ли одно квадратом второго.

def isSquare(firstNumber, secondNumber):
    if firstNumber == secondNumber ** 2:
        print(f'Число {firstNumber}(первое) являетя квадратом числа {secondNumber}(второго)')
    elif secondNumber == firstNumber ** 2:
        print(f'Число {secondNumber}(второе) являетя квадратом числа {firstNumber}(первого)')
    else:
        print(f'Ни одно число не является квадратом другого')

first_number = int(input('Введите целое число: '))
second_number = int(input('Введите целое число: '))
isSquare(first_number, second_number)