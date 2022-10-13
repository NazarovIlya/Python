# Создайте программу для игры в "Крестики-нолики".


game_map = [1, 2, 3,
            4, 5, 6,
            7, 8, 9]


win_lines = [[0, 1, 2,
              3, 4, 5,
              6, 7, 8,
              0, 3, 6,
              1, 4, 7,
              2, 5, 8,
              0, 4, 8,
              2, 4, 6]]


def output_game_map():
    print(game_map[:3])
    print(game_map[3:6])   
    print(game_map[6:9])  
    
    
def step_game_map(step, symbol):
      index = game_map.index(step)
      game_map[index] = symbol
      
      
def get_result():
    win = ""
    for i in win_lines:
        if game_map[i[0]] == "X" and game_map[i[1]] == "X" and game_map[i[2]] == "X":
            win = "X"
        if game_map[i[0]] == "O" and game_map[i[1]] == "O" and game_map[i[2]] == "O":
            win = "O"   
    return win


game_over = False
player_1 = True

while game_over == False:
    output_game_map()
    
    if player_1 == True:
        symbol = 'X'
        step = int(input('Игрок №1, Ваш ход: '))
    else:
        symbol = 'O'
        step = int(input('Игрок №2, Ваш ход: '))
        
    step_game_map(step, symbol)
    win = get_result()
    if win != '':
        game_over = True
    else:
        game_over = False
    
    player_1 = not(player_1)
    
    output_game_map()
    print('Победил, ', win)        
