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

def place_marker(board, marker, position):
    board[position] = marker