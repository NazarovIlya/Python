# Дан список чисел. Создайте список, в который попадают числа, описываемые
# возрастающую последовательность. Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.


def get_sequence_1(sequence):
    lst_1 = [sequence[0]]
    for i in range(0, len(sequence)):
        if sequence[i - 1] == sequence[i] - 1:
            lst_1.append(sequence[i - 1])
    return lst_1


def get_sequence_2(sequence):
    i = 0
    lst_2 = [sequence[0]]
    while i < len(sequence):
        for j in range(0, len(sequence)):
            if sequence[i - 1] + sequence[i] == sequence[j]:
                lst_2.append(sequence[j])
                i = sequence.index(sequence[j])
        i += 1
    return lst_2
        

lst = [1, 5, 2, 3, 4, 6, 1, 7]
print('Последовательность №1, сформированная по формуле A[n] = A[i] +  1: ', end= '')
result_1 = get_sequence_1(lst)
print(*result_1, sep= ', ')
print('Последовательность №2, сформированная по формуле A[n] = A[i] + A[i + 1]: ', end= '')
result_2 = get_sequence_2(lst)
print(*result_2, sep= ', ')
