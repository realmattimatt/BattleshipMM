# X for placing battleship and hit battleship
# ' ' for available spot
# '-' for missed shot
from random import randint

computer_board = [(' ') * 8 for x in range(8)] #Board not seen
player_board = [(' ') * 8 for x in range(8)]  #Board seen

letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}

def make_board(board):
    print('   A B C D E F G H')
    print('   ---------------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1
        

def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row] [ship_column] == 'X':
            ship_row, ship_column = randint(0,7), randint(0,7)
        # board[ship_row] [ship_column] = 'X'

def get_ship_location():
    row = input("Please enter a ship row 1-8: ")
    while row not in "12345678":
        print("Please enter a valid ship row number.")
        row = input("Please enter a ship row 1-8: ")
    column = input("Please enter a ship column A-H: ").upper()
    while column not in "ABCDEFGH":
        print("Please enter a valid ship column letter: ")
    return int(row) -1, letters_to_numbers[column]
        
    
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in board:
            if column == 'X':
                count += 1
    return count

create_ships(computer_board)
make_board(computer_board)
make_board(player_board)
turns = 10
# while turns > 0:
#     print("Ready to play Battleship")
# row, column = get_ship_location()
# if player_board[row][column] == '-':
#     print("You have already guessed that spot. Pick a different spot.")
# elif computer_board[row][column] == 'X':
#     print("Congradulations, you have hit a battleship")
#     player_board[row][column] = 'X' # type: ignore
#     turns -= 1
    



