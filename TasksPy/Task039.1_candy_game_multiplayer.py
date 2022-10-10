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


def player_motion(names, count, item):
    if count < 28:
        last_candy = count
    else:
        last_candy = 28
    if count > 0:
        motion = int(input(f'{names[item]}, Ваш ход. Выберите от 1 до {last_candy} конфет: '))
        if 1 <= motion <= 28:
            count -= motion
        else:
            print(f'{motion} конфет(ы) брать нельзя, переход хода.')
        if count == 0:
            print('Поздравляем! Вы забрали оставшиеся конфеты и выиграли их все.')
            quit()
    return count


def candy_game(names, count):
    last_candy = 28
    draw = random.randint(0, len(names) - 1)
    if draw == 1:
        motion = int(input(f'{names[draw]} начинает игру. Сделайте ход, возмите от 1 до {last_candy}: '))
        if  1 <= motion <= 28:
            count -= motion
        else:
            print(f'{motion} конфет(ы) брать  нельзя, переход хода.')
    while True:
        i = 0
        count = player_motion(names, count, i)
        i += 1
        count = player_motion(names, count, i)
        if count == 0:
            break
           

candy_count = int(input('Введите количество конфет, участвующих в игре: ')) #! 2021
player_count = 2
player_names = greeting(player_count)
candy_game(player_names, candy_count)


