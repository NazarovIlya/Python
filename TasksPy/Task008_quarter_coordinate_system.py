# Сообщить в какой четверти координатной плоскости или на какой
# оси находится точка с координатами Х и У.

x_coordinate = float(input('Введите значение координаты X: '))
y_coordinate = float(input('Введите значение координаты Y: '))

if x_coordinate != 0 or y_coordinate !=0:
    if x_coordinate > 0 and y_coordinate > 0:
        print(f'Точка с заданными координатами(x = {x_coordinate}, y = {y_coordinate}) лежит в первой плоскости.')
    elif x_coordinate < 0 and y_coordinate > 0:
        print(f'Точка с заданными координатами(x = {x_coordinate}, y = {y_coordinate}) лежит во второй плоскости.')
    elif x_coordinate < 0 and y_coordinate < 0:
        print(f'Точка с заданными координатами(x = {x_coordinate}, y = {y_coordinate}) лежит во третьей плоскости.')
    elif x_coordinate > 0 and y_coordinate < 0:
        print(f'Точка с заданными координатами(x = {x_coordinate}, y = {y_coordinate}) лежит во четвертой плоскости.')
else:
    print('Точка совпадает с точкой отсчета координат, X = 0, Y = 0')