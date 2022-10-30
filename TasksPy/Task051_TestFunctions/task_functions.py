# умножение ради теста ностроек рабочего окружения
def mult(a, b):
    return a * b


# По двум заданным числам проверить является ли одно квадратом второго.
def is_square(firstNumber, secondNumber):
    if firstNumber == secondNumber ** 2:
        return (f'Число {firstNumber}(первое) являетя квадратом числа {secondNumber}(второго)')
    elif secondNumber == firstNumber ** 2:
        return (f'Число {secondNumber}(второе) являетя квадратом числа {firstNumber}(первого)')
    else:
        return (f'Ни одно число не является квадратом другого')
    

# Найти максимальное из пяти чисел.   
def get_max(inputList):
    maxValue = inputList[0]
    for j in range(len(inputList)):
        if inputList[j] > maxValue:
            maxValue = inputList[j]
    return maxValue


# Вывести на экран числа от -N до N.
def sequence_minusN_to_N(numberN):
    lst = []
    if numberN > 0:                              # My solution
        minN = numberN * -1
    else:
        minN =  numberN
        numberN *= -1
    if numberN > minN:
        while minN <= numberN:
            lst.append(minN)
            minN += 1
    if numberN == 0:
        lst.append(0)
    return lst


# Показать первую цифру дробной части числа.
def get_first_float_digit(number):
    round_num = int(number)
    result = (number - round_num)*10
    return abs(int(result))
    