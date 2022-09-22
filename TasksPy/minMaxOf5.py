# Найти максимальное из пяти чисел.

inputList = []
for i in range(1,6):
    inputList.append(int(input(f'Введите целое число № {i}: ')))
maxValue = inputList[0]
for j in range(len(inputList)):
    if inputList[j] > maxValue:
        maxValue = inputList[j]
print(maxValue)