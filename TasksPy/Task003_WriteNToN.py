# Вывести на экран числа от -N до N.

numberN = int(input(f'Введите целое число: '))
# if numberN > 0:                           // My solution
#     minN = numberN * -1
# else:
#     minN =  numberN
#     numberN *= -1
# if numberN > minN:
#     while minN < numberN:
#         print(f'{minN} ', end = '')
#         minN += 1
# else: print(0)
for i in range(-numberN, numberN + 1):      # alternative solution
    print(f'{i} ', end = '')