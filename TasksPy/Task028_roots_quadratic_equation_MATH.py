# Найдите корни квадратного уравнения Ax² + Bx + C = 0 
# с помощью математических формул нахождения корней квадратного уравнения


def get_root_quadratic_equation(user_list):
    a, b, c = user_list
    discriminant = b ** 2 - 4 * a * c
    if discriminant == 0:
        x1 = -b / 2 * a
        x2 = x1
        return x1, x2
    elif discriminant > 0:
        x1 = (- b + discriminant ** 0.5) / 2 * a
        x2 = (- b - discriminant ** 0.5) / 2 * a
        return x1, x2
    else:
        return None, None
    
    
numbers_list = int(input('Введите значения квадратного многочлена: '))
a, b, c = numbers_list
get_root_quadratic_equation(a, b, c)
