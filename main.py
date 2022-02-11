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

def win_sum_calc(grid_num_format):        
    win_sums = []    
    for win in WIN_CONDITIONS:
        sum = 0
        for pos in win:
            sum += grid_num_format[pos]
        win_sums.append(sum)
    return win_sums

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# AI Possible Moves Functions

def ai_random_move():
    moved = False
    while not moved:
        pos = randint(0, 8)
        if grid[pos] == ' ': 
            grid[pos] = 'X'
            moved = True

def ai_block_win(losing_row):
    for pos in losing_row:
        if grid[pos] == ' ':
            grid[pos] = 'X'

def ai_winning_move(winning_row):
    for pos in winning_row:
        if grid[pos] == ' ':
            grid[pos] = 'X'

def ai_side_mid_move():
    moved = False
    while not moved:
        side_mid = random.choice([1, 3, 5, 7])
        if grid[side_mid] == ' ':
            grid[side_mid] = 'X'
            moved = True
