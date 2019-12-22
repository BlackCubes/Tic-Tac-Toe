# Tic-Tac-Toe
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

![The result when winning the game](winner.png)

## Installation

To play the game, download `tic-tac-toe.py` and save it on whatever destination you wish to have it on. For Mac, run your Terminal, go to the file destination where you saved it, and run the command `python tic-tac-toe.py`. For Windows, it is the same procedure, but find `cmd` in your Windows search, run it and repeat the process.

## Documentation

This game was created while learning from a Udemy course `Complete Python Bootcamp: Go from zero to hero in Python 3` by `Jose Portilla`. It is a simple gameplay utilizing the rules of Tic-Tac-Toe: Whomever gets the same three marks in role vertically, horizontally, or diagonally wins the game.

#### Imports

I imported two modules called `random` and `time` to be used later by utilizing `random.randint()` and `time.sleep()`. `random.randint()` randomizes the numbers based on the range inside its arguments while `time.sleep()` pauses the system based on the amount of time (in seconds) you pass in the argument.

#### Functions

The function `display_board(board)` creates a mark-up of the Tic-Tac-Toe game by generating a 3x3 by utilizing the `print()` function. It takes in a 1D array as an argument and places the indexes at the 'bottom-left' of the board (starting at index 1), and works its way up from left-to-right and bottom-to-top:

```
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
```

Next is the function `player_input()` which asks the first player which marker she/he wants to be (`X` or `O`) and returns that marker. If the player does not properly input the marker, then the question repeats itself until it is correct:

```
def player_input():
    bool_value = 0

    while bool_value < 1:
        player1 = input("Player 1, please pick a marker 'X' or 'O' ")
        if player1.upper() == 'X' or player1.upper() == 'O':
            bool_value = 1
            return player1.upper()
        else:
            bool_value = 0
```

The next function is `place_marker(board, marker, position)` which changes the value of the board array based on the index from the player's position choice:

```
def place_marker(board, marker, position):
    board[position] = marker
```

The next function `win_check(board, mark)` checks to see if the player won on the board based on the marker. The first thing it does is convert the 1D board array into a 2D board array, and it does this with the implementation of multi-arrays thus creating a 3x3 board simulation:

```
[board[1:][r*3:(r+1)*3] for r in range(0,3)]
```

`r` is how many rows you want while the `3` multiplication is how many columns you want. It gets the 2D board height by using `len(new_board)`, and it gets the 2D board width by using `len(new_board[0])` (or the length of the inner first index). After this is a nested for-loop which finds the same three marks horizontally, vertically, or diagonally. This is done mathematically (like a nxm matrix) where `[y]` stays constant while `[x]` increases by 1 for finding the horizontal; the `[y]` increases by 1 while the `[x]` stays constant for finding the vertical; both `[x]` and `[y]` both increase by one for the diagonal starting from the bottom-left corner; and `[y]` increases by one while `[x+2]` decreases by one for the diagonal starting from the top left corner. An `IndexError` might occur since the index could be out of range, and so a `try-except` case is considered. If it finds any three consecutive marks then it returns `True`, or `False` otherwise:

```
def win_check(board, mark):
    new_board = [board[1:][r*3:(r+1)*3] for r in range(0,3)]

    board_height = len(new_board)
    board_width = len(new_board[0])

    for y in range(board_height):
        for x in range(board_width):
            try:
                if new_board[y][x] == mark and new_board[y][x+1] == mark and new_board[y][x+2] == mark:
                    return True
            except IndexError:
                next

    for y in range(board_height):
        for x in range(board_width):
            try:
                if new_board[y][x] == mark and new_board[y+1][x] == mark and new_board[y+2][x] == mark:
                    return True
            except IndexError:
                next

    for y in range(board_height):
        for x in range(board_width):
            try:
                if new_board[y][x] == mark and new_board[y+1][x+1] == mark and new_board[y+2][x+2] == mark:
                    return True
            except IndexError:
                next

    for y in range(board_height):
        for x in range(board_width):
            try:
                if new_board[y][x+2] == mark and new_board[y+1][x+1] == mark and new_board[y+2][x] == mark:
                    return True
            except IndexError:
                next

    return False
```

The next function randomizes which player should go first by using the `random` module. It returns a tuple of variables to be used when putting the game together:

```
def choose_first():
    rand_player_int = random.randint(1,2)
    rand_player_str = 'Player {} goes first!'.format(rand_player_int)

    return rand_player_int, rand_player_str
```

This function checks if the space on the board is free. Returns `True` if there is space, but `False` otherwise:

```
def space_check(board, position):
    return board[position].isspace()
```

The next function checks if the board is full. Returns `True` if it is full, but `False` otherwise:

```
def full_board_check(board):
    bool_value = True

    for full in board:
        if full.isspace():
            bool_value = False

    return bool_value
```

The next function asks the current player on which position she/he would like to place their marker. Once the player inputs their decision, it checks if that space is empty by utilizing the function `space_check(board, position)`. Returns the player's position if `True`:

```
def player_choice(board):
    bool_value = 0

    while bool_value < 1:
        position = int(input('Choose your next position: (1-9) '))
        if space_check(board, position):
            bool_value = 1
            return position
        else:
            bool_value = 0
```

The last function asks the player(s) if they would like play the game again. It handles different edge cases like `yes` or `y`. Returns `True` if the player(s) do want to play again, `False` if they do not, and the prompt keeps asking until the conditionals are met:

```
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
```

And that is all towards making the Tic-Tac-Toe game!

## Conclusions

Many thanks to anyone visiting this repository, and many thanks to `Jose Portilla` for inspiring and helping others to learn and become a better programmer. Remember to keep pushing no matter what and if you are alone.