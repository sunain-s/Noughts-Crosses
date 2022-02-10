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

def check_move(move):
    valid_move = False
    if grid[move] == ' ':
        valid_move = True
    else:
        print('Invalid move, choose elsewhere.')
    return valid_move

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

def check_move(move):
    valid_move = False
    if grid[move] == ' ':
        valid_move = True
    else:
        print('Invalid move, choose elsewhere.')
    return valid_move

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Cell + Row Value Calculation Functions  

def cell_values():
    grid_num_format = []
    for cell in grid:
        if cell == ' ':
            grid_num_format.append(0)
        elif cell == 'X':
            grid_num_format.append(1)
        elif cell == 'O':
            grid_num_format.append(-1)
    return grid_num_format 
