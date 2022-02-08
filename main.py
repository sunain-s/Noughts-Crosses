# Noughts and Crosses (Tic Tac Toe)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Imports 

import random
from random import randint

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Move Input Functions

def input_move():
    move = int(input('Enter number 1-9:  '))
    move -= 1
    valid_move = check_move(move)
    if valid_move:
        grid[move] = 'O'
    return valid_move
