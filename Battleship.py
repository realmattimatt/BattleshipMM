import random

length_of_ships = [2,3,3,4,5,]
computer_board = [[' '] * 8 for x in range(8)]
player_board = [[' '] * 8 for x in range(8)]
player_guess_board = [[' '] * 8 for x in range(8)]
computer_guess_board = [[' '] * 8 for x in range(8)]
letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}

def print_board(board):
    print('   A B C D E F G H')
    print('   ---------------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def place_ships(board):
    for ship_length in length_of_ships:
        while True:
            if board == computer_board:
                orientation, row, column = random.choice(["H","V"]), random.randint(0,7), random.randint(0,7)
                if check_ship_fit(ship_length, row, column, orientation):
                    if ship_overlap(board, row, column, orientation, ship_length) == False:
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                        break
            else:
                place_ship = True
                print("Place a ship with a length of " + str(ship_length))
                row, column, orientation = user_input(place_ship)
                if check_ship_fit(ship_length, row, column, orientation):
                    if ship_overlap(board, row, column, orientation, ship_length) == False:
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                        print(player_board)
                        break                                           

def check_ship_fit(ship_length, row, column, orientation):
    if orientation == "H":
        if column + ship_length > 8:
            return False
        else:
            return True
    else:
        if row + ship_length > 8:
            return False
        else:
            return True

def ship_overlap(board, row, column, orientation, ship_length):
    if orientation == "H":
        for i in range(column, column + ship_length):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row + ship_length):
            if board[i][column] == "X":
                return True
    return False

def user_input(place_ship):
    if place_ship == True:
        while True:
            try:
                orientation = input("Enter ship orientation (H or V): ").upper()
                if orientation == "H" or orientation == "V":
                    break
            except TypeError:
                print("Enter a valid entry H or V")
        while True:
            try:
                row = input("Enter the row 1-8 for the ship: ")
                if row in "12345678":
                    row = int(row) -1
                    break
            except ValueError:
                print("Enter a valid number form 1-8")
        while True:
            try:
                column = input("Enter the column of the ship: ").upper()
                if column in "ABCDEFGH":
                    column = letters_to_numbers[column]
                    break
            except KeyError:
                print("Enter a valid letter between A-H")
        return row, column, orientation
    else:
        while True:
            try:
                row = input("Enter the row 1-8 for the ship: ")
                if row in "12345678":
                    row = int(row) - 1
                    break
            except ValueError:
                print("Enter a valid number between 1 - 8")
        while True:
            try:    
                column = input("Enter the column for the ship: ").upper()
                if column in "ABCDEFGH":
                    column = letters_to_numbers[column]
                    break
            except KeyError:
                print("Enter a valid letter between A-H")
        return row, column                  

def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

def turn(board):
    if board == player_guess_board:
        row, column = user_input(player_guess_board)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif computer_board[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"
    else:
        row, column = random.randint(0,7), random.randint(0,7)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif player_board[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"

place_ships(computer_board)
print_board(computer_board)
print_board(player_board)
place_ships(player_board)              

while True:
    while True:
        print("Guess a battleship spot")
        print_board(player_guess_board)
        turn(player_guess_board)
        break
    if count_hit_ships(player_guess_board) == 17:
        print("You won!!!")
        break
    while True:
        turn(computer_guess_board)
        break
    print_board(computer_guess_board)
    if count_hit_ships(computer_guess_board) == 17:
        print("The computer won, please try again")
        break
