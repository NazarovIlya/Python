def mult(a, b):
    return a * b


def is_square(firstNumber, secondNumber):
    if firstNumber == secondNumber ** 2:
        return (f'Число {firstNumber}(первое) являетя квадратом числа {secondNumber}(второго)')
    elif secondNumber == firstNumber ** 2:
        return (f'Число {secondNumber}(второе) являетя квадратом числа {firstNumber}(первого)')
    else:
        return (f'Ни одно число не является квадратом другого')
    
    
def get_max(inputList):
    maxValue = inputList[0]
    for j in range(len(inputList)):
        if inputList[j] > maxValue:
            maxValue = inputList[j]
    return maxValue