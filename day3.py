import numpy as np

# importing the input data into a grid and also collecting unique symbols used
with open('day3_input.txt') as f:
    grid = np.array([[y for y in x] for x in [x.rstrip('\n') for x in f.readlines()]])
    f.seek(0)
    symbols = set([x for x in f.read() if not x.isdigit() and x != '\n' and x != '.'])


# ---------------- part 1  ----------------

# function to check if there is a symbol in 8 cells (or less) around a particular cell
def symbolNear(row, col):
    state = False
    
    if(grid[max(0, row-1)][max(0, col-1)] in symbols or 
       grid[max(0, row-1)][col] in symbols or
       grid[max(0, row-1)][min(col+1, grid.shape[1]-1)] in symbols or
       grid[row][max(0, col-1)] in symbols or
       grid[row][min(col+1, grid.shape[1]-1)] in symbols or
       grid[min(grid.shape[0]-1, row+1)][max(0, col-1)] in symbols or 
       grid[min(grid.shape[0]-1, row+1)][col] in symbols or
       grid[min(grid.shape[0]-1, row+1)][min(col+1, grid.shape[1]-1)] in symbols       
       ):
        state = True
    return state

      
current_number = 0
is_part = False
answer = 0

# going from through the grid by each cell
for row in range(grid.shape[0]):
    for col in range(grid.shape[1]):
        
        # if cell is a digit, construct the number and check if there is symbol around
        if grid[row][col].isdigit():
            current_number = current_number * 10 + int(grid[row][col])
            if symbolNear(row, col):
                is_part = True
        
        # if cell is not a digit, check if it's "part" and add to answer
        if not grid[row][col].isdigit() or col == grid.shape[0]:
            if is_part:
                answer += current_number
            current_number = 0
            is_part = False
            
print('answer for part one is {}'.format(answer))
        


# ---------------- part 2  ----------------

# function to extract the full number
def findNumber(row, col):
    if grid[row][col].isdigit():
        
        # find left-most position for number
        col_pos = col
        while col_pos > 0 and grid[row][col_pos-1].isdigit():
            col_pos -= 1
        
        # find number:
        number = 0
        col_move = col_pos
        while col_move < grid.shape[1] and grid[row][col_move].isdigit():
            number = number * 10 + int(grid[row][col_move])
            col_move += 1
            
        # return starting position of the number and number as a tuple
        return row, col_pos, number
        
    else:
        return None
    
answer2 = 0

# scan through the grid by checking each cell
for row in range(grid.shape[0]):
    for col in range(grid.shape[1]):
        if grid[row][col] ==  '*':
            found_numbers = []
            
            # find numbers in all 8 (if possible) cells around *
            if row > 0 and col > 0:
                found_numbers.append(findNumber(row-1, col-1))
            if row > 0:
                found_numbers.append(findNumber(row-1, col))
            if row > 0 and col < grid.shape[1]:
                found_numbers.append(findNumber(row-1, col+1))
                
            if col > 0:
                found_numbers.append(findNumber(row, col-1))
            if col < grid.shape[1]:
                found_numbers.append(findNumber(row, col+1))
                
            if row < grid.shape[0] and col > 0:
                found_numbers.append(findNumber(row+1, col-1))
            if row < grid.shape[0]:
                found_numbers.append(findNumber(row+1, col))
            if row < grid.shape[0] and col < grid.shape[1]:
                found_numbers.append(findNumber(row+1, col+1))
                
            # remove numbers found multiple times
            found_numbers = list(dict.fromkeys([x for x in found_numbers if x is not None]))
            
            if len(found_numbers) > 1:
                answer2 += found_numbers[0][2] * found_numbers[1][2]

print('answer for part two is {}'.format(answer2))