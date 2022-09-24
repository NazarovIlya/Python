# Найти расстояние между двумя точками пространства.

from turtle import distance


def find_distance(x1_coord, y1_coord, x2_coord, y2_coord):
        d_x = ((x2_coord - x1_coord) ** 2)
        d_y = ((y2_coord - y1_coord) ** 2) 
        result_distance = (d_x + d_y) ** 0.5
        return result_distance

x1_coord = float(input('Введите значение координаты X первой точки: '))
y1_coord = float(input('Введите значение координаты Y первой точки: '))
x2_coord = float(input('Введите значение координаты X второй точки: '))
y2_coord = float(input('Введите значение координаты Y второй точки: '))
print(f'{round(find_distance(x1_coord, y1_coord, x2_coord, y2_coord), 3)}')