# Сообщить в какой четверти координатной плоскости или на какой
# оси находится точка с координатами Х и У.

def find_dimension(x_coordinate, y_coordinate):
    if x_coordinate != 0 or y_coordinate !=0:
        if x_coordinate > 0 and y_coordinate > 0:
            print(f'Точка с заданными координатами(x = {x_coordinate}, y = {y_coordinate}) лежит в первой плоскости.')
        elif x_coordinate < 0 and y_coordinate > 0:
            print(f'Точка с заданными координатами(x = {x_coordinate}, y = {y_coordinate}) лежит во второй плоскости.')
        elif x_coordinate < 0 and y_coordinate < 0:
            print(f'Точка с заданными координатами(x = {x_coordinate}, y = {y_coordinate}) лежит в третьей плоскости.')
        elif x_coordinate > 0 and y_coordinate < 0:
            print(f'Точка с заданными координатами(x = {x_coordinate}, y = {y_coordinate}) лежит в четвертой плоскости.')
    else:
        print('Точка совпадает с точкой отсчета координат, X = 0, Y = 0')
        
x_coord = float(input('Введите значение координаты X: '))
y_coord = float(input('Введите значение координаты Y: '))
find_dimension(x_coord, y_coord)
