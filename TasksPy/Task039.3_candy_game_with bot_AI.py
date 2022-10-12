# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: 
# На столе лежит 2021 конфета. Играют два игрока делая ход друг
# после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не
# более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего
# конкурента?
# 
# a) Добавьте игру против бота
#* b) Подумайте как наделить бота "интеллектом"
#
#! Игра с простым ботом с искусственным интеллектом


import random
from time import sleep


def greeting():
    names_list = ['Bot']
    names_list.append(input(f'Вы играете с ботом. Введите свое имя: '))
    print(f'Привет, {names_list[1]}')
    return names_list


def first_motion(names, count, max_count_for_motion):
    while True:
        last_candy = max_count_for_motion
        draw = random.randint(0, len(names) - 1)
        if draw == 1:
            motion = int(input(f'{names[draw]} начинает игру и делает первый ход. Можно взять от 1 до {last_candy}: '))
            if  1 <= motion <= max_count_for_motion:
                    count -= motion
                    return count, draw
            else:
                print(f'{motion} конфет(ы) брать нельзя, введите корректное значение.')
        else:
            print(f'Ходит {names[draw]}')
            motion = bot_AI_motion(count, last_candy)
            count -= motion
            print(f'{names[draw]} сходил.')
            return count, draw


def user_motion_input(names, last_candy, item):
    while True:
        if item == 1:
            motion = int(input(f'{names[item]}, Ваш ход. Возьмите от 1 до {last_candy} конфет: '))
            if motion <= last_candy:
                if 1 <= motion <= 28:
                    return motion
                else:
                    print(f'{motion} конфет(ы) брать нельзя, введите корректное значение.')
            
            
def bot_AI_motion(count, max_candy_count):
    if count > max_candy_count * 2:
        bot_random_count = random.randint(1, max_candy_count)
        return bot_random_count
    elif count <= max_candy_count:
        return count
    else:
        atemp = count // max_candy_count
        if atemp == 2:
            count = count // 2
            return count
        else:
            return count - (max_candy_count + 1)
        

def bot_player_motion(names, count, item, max_count_for_motion):
    if item == 1:
        if count < max_count_for_motion:
            last_candy = count
        else:
            last_candy = max_count_for_motion
        if count > 0:
            motion = user_motion_input(names, last_candy, item)
            if 1 <= motion <= max_count_for_motion:
                count -= motion
    else:
        if count < max_count_for_motion:
            last_candy = count
        else:
            last_candy = max_count_for_motion
        if count > 0:
            print(f'Ходит {names[item]}', end= '...')
            motion = bot_AI_motion(count, last_candy)
            count -= motion
            sleep(1)
            print(f'{names[item]} сходил.')
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
        
        
def game_over(count, item):
    if count == 0:
        if item == 1:
            print('Поздравляем! Вы забрали оставшиеся конфеты и выиграли их все.')
            quit()
        else:
            print('Выиграл бот. Попробуйте еще раз.')
            quit()
    return
        

def candy_game(names, count, max_count_for_motion):
    count, first_item = first_motion(names, count, max_count_for_motion)
    current_item = check_item(first_item)
    while True:
        print(f'На столе осталось {count} конфет.')
        count = bot_player_motion(names, count, current_item, max_count_for_motion)
        game_over(count, current_item)
        current_item = check_item(current_item)
        

    
           
max_candy_count = 28 #!
candy_count = int(input('Введите количество конфет, участвующих в игре: ')) #! 2021
check_candy_count(candy_count, max_candy_count)
player_names = greeting()
candy_game(player_names, candy_count, max_candy_count)