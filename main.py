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

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Master AI Move Select Function

def ai_moves(win_sums):
    if 2 in win_sums:
        winning_row = WIN_CONDITIONS[win_sums.index(2)]
        ai_winning_move(winning_row)

    elif -2 in win_sums:
        losing_row = WIN_CONDITIONS[win_sums.index(-2)]
        ai_block_win(losing_row)

    elif grid[4] == ' ':
        grid[4] = 'X'

    elif grid[4] == 'O':
        corner = random.choice([0, 2, 6, 8])
        if grid[corner] == ' ':
            grid[corner] = 'X'
        
    elif (grid[0] == 'O' and grid[8] == 'O') or (grid[2] == 'O' and grid[6] == 'O'):
        ai_side_mid_move() 

    else:
        ai_random_move()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Output + End Game Functions

def check_win(win_sums):
    for i in win_sums:
        if i == -3:
            print('\n\nNoughts win')
            return True
        if i == 3:
            print('\n\nCrosses win')
            return True

    if ' ' not in grid:
        print('\n\nDraw')
        return True
    return False
