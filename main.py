# TicTacToe - version 1.55

from random import randrange
import os

def display_board(board): # rysuje plansze
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    for i in range(3):
        print("+-------+-------+-------+", "|       |       |       |", sep="\n")
        for j in range(3):
            print("|   ", board[i][j], "   ",sep="", end="")
        print("|", "|       |       |       |" , sep="\n")
    print("+-------+-------+-------+")

def make_list_of_free_fields(board): # sprawdza które pola są wolne
    free_areas = []
    for i in range(3):
        for j in range(3):
            if type(board[i][j]) is int:
                tuple = (i, j)
                free_areas.append(tuple)
    return free_areas

def enter_move(board): # ruch gracza
    free_areas = make_list_of_free_fields(board)
    dictionaly = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2)}
    for i in range(1, 10):
        if dictionaly[i] not in free_areas:
            del dictionaly[i]
    
    input_value = int(input("Podaj numer pola: "))
    if not (input_value > 0 or input_value < 10):
        return
    
    value1 = dictionaly[input_value][0]
    value2 = dictionaly[input_value][1]
    board[value1][value2] = "O"
    return board

def victory_for(board): # funkcja sprawdza kto wygrał
    boolean = True
    for i in range(3):
        for j in range(3):
            if type(board[i][j]) is not int:
                continue
            else:
                boolean = False

    # do poprawy sprawdzanie wygranego              
    if (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") or (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X") or (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X") or (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X") or (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") or (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X") or (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X"):
        return "Przegrałeś...Nie dobrze..."
    elif (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O") or (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O") or (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O") or (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O") or (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O") or (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O") or (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O") or (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X"):
        return "Wygrałeś... Brawo!"
    elif boolean == True:
        return "No to mamy remis..." 
    else:
        return 0

def draw_move(board): # ruch komputera
    free_areas = make_list_of_free_fields(board)
    if len(free_areas) == 9:
        board[1][1] = "X"
        display_board(board)
        return board
    random = randrange(len(free_areas))
    value1 = free_areas[random][0]
    value2 = free_areas[random][1]
    board[value1][value2] = "X"
    display_board(board)
    return board

board = [[1,2,3],[4,5,6],[7,8,9]]

if __name__ == '__main__':
    while True:
        board = draw_move(board)
        result = victory_for(board)
        if result != 0:
            print(result)
            break
        board = enter_move(board)
        result = victory_for(board)
        if result != 0:
            print(result)
            break
