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



# Create a function that checks if there are no spaces on the board
def full_board_check(board):
    bool_value = True

    for full in board:
        if full.isspace():
            bool_value = False

    return bool_value



# Create a function asking for the player's next position, and also checks if the space is empty by using the space_check function
def player_choice(board):
    bool_value = 0

    while bool_value < 1:
        position = int(input('Choose your next position: (1-9) '))
        if space_check(board, position):
            bool_value = 1
            return position
        else:
            bool_value = 0



# Create a function that asks the player if they want to play the game after finishing
def replay():
    bool_value = 0

    while bool_value < 1:
        replay_input = input('Do you want to play again? (Yes/No) ')
        if replay_input.lower() == 'yes' or replay_input.lower() == 'y':
            bool_value = 1
            return True
        elif replay_input.lower() == 'no' or replay_input.lower() == 'n':
            bool_value = 1
            return False
        else:
            bool_value = 0



# Put everything together and create the game

while True:

    #Set up the game

    tic_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    game_on = True

    player1_marker = player_input()
    player2_marker = ''

    if player1_marker == 'X':
        player2_marker = 'O'
    else:
        player2_marker = 'X'

    print("Player 1 picked '{}', and Player 2 gets '{}'".format(player1_marker, player2_marker))

    time.sleep(2.5)
    print("Let's see who goes first...")
    time.sleep(2)

    # Remember to get the tuple results to be used from choose_first function:
    rand_player_int, rand_player_str = choose_first()

    print(rand_player_str)

    time.sleep(2)
    print('Here comes the board! Have fun :)')
    time.sleep(1.4)

    display_board(tic_board)

    while game_on:

        # Player 1's turn
        if rand_player_int == 1:

            print('\n'*100)

            print("\nPLAYER 1\n")

            display_board(tic_board)

            print("\n")

            player1_position = player_choice(tic_board)

            place_marker(tic_board, player1_marker, player1_position)

            # Check if winner, the board is full, or continue the game to the next player
            if win_check(tic_board, player1_marker):
                print('\n'*100)
                display_board(tic_board)
                print("\nPlayer 1 wins!")
                game_on = False
                continue
            elif full_board_check(tic_board):
                print('\n'*100)
                display_board(tic_board)
                print("\nLooks like we have a tie :( WAH! WAH!")
                game_on = False
                continue
            else:
                rand_player_int = 2
                continue

        # Player 2's turn
        elif rand_player_int == 2:

            print('\n'*100)

            print("\n\n")

            display_board(tic_board)

            print("\nPLAYER 2")

            player2_position = player_choice(tic_board)

            place_marker(tic_board, player2_marker, player2_position)

            if win_check(tic_board, player2_marker):
                print('\n'*100)
                display_board(tic_board)
                print("\nPlayer 2 wins!")
                game_on = False
                continue
            elif full_board_check(tic_board):
                print('\n'*100)
                display_board(tic_board)
                print("\nLooks like we have a tie :( WAH! WAH!")
                game_on = False
                continue
            else:
                rand_player_int = 1
                continue

    # Check if the players want to replay the game
    else:
        if not replay():
            False
            break
        else:
            True
            continue