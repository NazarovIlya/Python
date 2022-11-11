# Дана функция f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
# 1. Определить корни
# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает
# 4. Построить график
# 5. Вычислить вершину
# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0

# import matplotlib
import matplotlib.pyplot as plt
import numpy as np
#import sympy as sp


# Определить корни
def f(x):
    return -12 * x ** 4 * np.sin(np.cos(x)) - \
         18 * x ** 3 + 5 * x ** 2 + 10 * x - 30
    

# График функции при помощи библиотеки matplotlib:
def function_graph(min, max):
     x = [x for x in range(min, max)]
     y = [(-12 * x ** 4 * np.sin(np.cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30) for
          x in range(min, max)]
     # y = [y for y in range(min, max)]
     plt.plot(x, y)
     plt.grid()
     plt.show()


min = -100
max = 100