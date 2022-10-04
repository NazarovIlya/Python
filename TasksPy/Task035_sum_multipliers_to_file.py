# Даны два файла, в каждом из которых находится запись многочлена. Задача -
# сформировать файл, содержащий сумму многочленов.


with open('./task035/file1.txt', 'r') as f1:
    file_list_1 = f1.readline().split()
    print(file_list_1)
with open('./task035/file2.txt', 'r') as f2:
    file_list_2 = f2.readline().split()
    print(file_list_2)
multiple_1 = file_list_1
multiple_2 = file_list_2
a1 = int(multiple_1[0][0])
b1 = int(multiple_1[2][0])
c1 = int(multiple_1[4])
a2 = int(multiple_2[0][0])
b2 = int(multiple_2[2][0])
c2 = int(multiple_2[4])
a = a1 + a2
b = b1 + b2
c = c1 + c2
degree = int(multiple_1[0][3])


with open('./task035/result.txt', 'w') as new_f:
    new_f.write(f'{a}x^{degree} + {b}x + {c} = 0')
