# Задача 1. Создайте программу для игры в "Крестики-нолики".
count_step = 0

field_game = [1, 2, 3, 4, 5, 6, 7, 8, 9]

victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]

def print_field(field):
    for i in range(0, len(field), 3):
        print(field[i], end=" ")
        print(field[i + 1], end=" ")
        print(field[i + 2])

def step_field(step, symbol):
    ind = field_game.index(step)
    field_game[ind] = symbol

def get_result():
    win = ""
    for i in victories:
        if field_game[i[0]] == "X" and field_game[i[1]] == "X" and field_game[i[2]] == "X":
            win = "X"
        if field_game[i[0]] == "O" and field_game[i[1]] == "O" and field_game[i[2]] == "O":
            win = "O"
    return win

game_over = False
player1 = True

while game_over == False:
    print_field(field_game)
    if player1 == True: # ход игрока
        symbol = "X"
        step = int(input("Человек 1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Человек 2, ваш ход: "))

    step_field(step, symbol)  # делаем ход в указанную ячейку
    count_step += 1
    win = get_result()  # определим победителя
    str_mes = ""
    if win != "":
        game_over = True
        str_mes = "Победитель " + win
    elif win == "" and count_step == 9:
        game_over = True
        str_mes = "Победила дружба!"
    else:
        game_over = False
    player1 = not (player1)

print_field(field_game)
print(str_mes)


