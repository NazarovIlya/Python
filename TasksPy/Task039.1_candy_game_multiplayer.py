#
# Создайте программу для игры с конфетами #* человек против человека.
# Условие задачи: 
# На столе лежит 2021 конфета. Играют два игрока делая ход друг
# после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не
# более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего
# конкурента?
# 
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
#
#! Мультиплеер


import random


def greeting(player_count):
    names_list = []
    for i in range(player_count):
        names_list.append(input(f'Введите имя игрока №{i + 1}: '))
        print(f'Привет, {names_list[i]}')
    return names_list


def first_motion(names, count, max_count_for_motion):
    while True:
        last_candy = max_count_for_motion
        draw = random.randint(0, len(names) - 1)
        motion = int(input(f'{names[draw]} начинает игру. Сделайте ход, возмите от 1 до {last_candy}: '))
        if  1 <= motion <= max_count_for_motion:
                count -= motion
                return count, draw
        else:
            print(f'{motion} конфет(ы) брать нельзя, введите корректное значение.')


def user_motion_input(names, last_candy, item):
    while True:
        motion = int(input(f'{names[item]}, Ваш ход. Выберите от 1 до {last_candy} конфет: '))
        if motion <= last_candy:
            if 1 <= motion <= 28:
                return motion
            else:
                print(f'{motion} конфет(ы) брать нельзя, введите корректное значение.')


def player_motion(names, count, item, max_count_for_motion):
    if count < max_count_for_motion:
        last_candy = count
    else:
        last_candy = max_count_for_motion
    if count > 0:
        motion = user_motion_input(names, last_candy, item)
        if 1 <= motion <= max_count_for_motion:
            count -= motion
    return count


def check_item(current_item):
    if current_item == 0:
        current_item = 1
        return current_item
    else:
        current_item = 0
        return current_item    
    

def check_candy_count(candy_count, max_count_for_motion):
    count = max_count_for_motion * 2 + 2
    if candy_count < count:
        print(f'Ошибка ввода. Количество конфет должно быть не меньше {count}.')
        quit()
        
        
def game_over(count):
    if count == 0:
        print('Поздравляем! Вы забрали оставшиеся конфеты и выиграли их все.')
        quit()
        

def candy_game(names, count, max_count_for_motion):
    count, first_item = first_motion(names, count, max_count_for_motion)
    current_item = check_item(first_item)
    while True:
        print(f'На столе осталось {count} конфет.')
        count = player_motion(names, count, current_item, max_count_for_motion)
        current_item = check_item(current_item)
        game_over(count)

    
           
player_count = 2 #!
max_candy_count = 28 #!
candy_count = int(input('Введите количество конфет, участвующих в игре: ')) #! 2021
check_candy_count(candy_count, max_candy_count)
player_names = greeting(player_count)
candy_game(player_names, candy_count, max_candy_count)



