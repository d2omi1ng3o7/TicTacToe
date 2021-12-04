from random import randrange

def generator_board(): # generuje listę z planszą gry
    board = []
    number = 0
    for i in range(3):
        row = [number + i + 1 for i in range(3)]
        board.append(row)
        number += 3
    return board

def display_board(board): # rysuje plansze
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
    
    input_value = int(input("Podaj liczbę odpowiadającą numerze pola które chcesz wybrać: "))
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
        return "P"
    elif (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O") or (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O") or (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O") or (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O") or (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O") or (board[0][0] == "O" and board[1][0] == "O" and board[1][0] == "O") or (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O") or (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X"):
        return "W"
    elif boolean == True:
        return "R" 
    else:
        return None

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
    
board = generator_board()
while True:
    board = draw_move(board)
    result = victory_for(board)
    
    if result == None:
        pass
    elif result == "R":
        print("No to kurwa mamy pata...")
        break
    elif result == "P":
        print("Przejebałeś z debilem nie dobrze...")
        break
    elif result == "W":
        print("Wygrałeś bilety na chuja z gazety...Brawo!")
        break
    
    board = enter_move(board)
    result = victory_for(board)
    if result == None:
        pass
    elif result == "R":
        print("No to kurwa mamy pata...")
        break
    elif result == "P":
        print("Przejebałeś z debilem nie dobrze...")
        break
    elif result == "W":
        print("Wygrałeś bilety na chuja z gazety...Brawo!")
        break