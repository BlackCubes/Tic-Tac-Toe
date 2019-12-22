# Import random and time to be used later
import random
import time



# Create the tic-tac-toe board that is 3x3. In the middle are values
def display_board(board):
    print("   |   |   ")
    print(" {} | {} | {}".format(board[7],board[8],board[9]))
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" {} | {} | {}".format(board[4],board[5],board[6]))
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" {} | {} | {}".format(board[1],board[2],board[3]))
    print("   |   |   ")



# Create a function that takes in the player's input
def player_input():
    # Boolean Int Value that breaks/continues the while loop
    bool_value = 0

    # Loop the input until the player correctly answers, and return it for later
    while bool_value < 1:
        player1 = input("Player 1, please pick a marker 'X' or 'O' ")
        if player1.upper() == 'X' or player1.upper() == 'O':
            bool_value = 1
            return player1.upper()
        else:
            bool_value = 0



# Change the board list value by its index
def place_marker(board, marker, position):
    board[position] = marker



# Create a function that checks if the player won based on their marker
def win_check(board, mark):
    # Create a 3x3 array from the board list without its index 0. This would simulate the actual 2D game and find the winning score
    new_board = [board[1:][r*3:(r+1)*3] for r in range(0,3)]

    board_height = len(new_board)
    board_width = len(new_board[0])

    # Find the Horizontal Win without IndexError
    for y in range(board_height):
        for x in range(board_width):
            try:
                if new_board[y][x] == mark and new_board[y][x+1] == mark and new_board[y][x+2] == mark:
                    return True
            except IndexError:
                next

    # Find the Vertical Win without IndexError
    for y in range(board_height):
        for x in range(board_width):
            try:
                if new_board[y][x] == mark and new_board[y+1][x] == mark and new_board[y+2][x] == mark:
                    return True
            except IndexError:
                next

    # Find one side of the Diagonal Win starting from the bottom left without IndexError
    for y in range(board_height):
        for x in range(board_width):
            try:
                if new_board[y][x] == mark and new_board[y+1][x+1] == mark and new_board[y+2][x+2] == mark:
                    return True
            except IndexError:
                next

    # Find other side of the Diagonal Win starting from the top left without IndexError
    for y in range(board_height):
        for x in range(board_width):
            try:
                if new_board[y][x+2] == mark and new_board[y+1][x+1] == mark and new_board[y+2][x] == mark:
                    return True
            except IndexError:
                next

    return False



# Create a function that randomizes which player goes first
def choose_first():
    rand_player_int = random.randint(1,2)
    rand_player_str = 'Player {} goes first!'.format(rand_player_int)

    # Return as a tuple for both to be used later
    return rand_player_int, rand_player_str



# Create a function that checks if the space on the board is free
def space_check(board, position):
    return board[position].isspace()