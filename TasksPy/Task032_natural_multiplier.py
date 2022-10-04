# Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.


def get_sequence_natural_multiplier(number):
   i = 2
   multiplier_list = []
   while i * i <= number:
       while number % i == 0:
           multiplier_list.append(i)
           number = number // i
       i += 1
   if number > 1:
       multiplier_list.append(number)
   return multiplier_list
    
    
num = int(input('Введите любое натуральное число: '))
result = get_sequence_natural_multiplier(num)
print(f'Число {num} состоит из простых множителей: {result}')