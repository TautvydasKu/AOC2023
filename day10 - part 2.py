import numpy as np
import sys

sys.setrecursionlimit(20000)

with open('day10_input.txt') as f:
    grid = np.array([[y for y in x] for x in [x.rstrip('\n') for x in f.readlines()]])
    
for y in range(grid.shape[0]):
    for x in range(grid.shape[1]):
        if grid[y][x] == 'S':
            s_y = y
            s_x = x
print('starting position: y = {}, x = {}'.format(s_y, s_x))
print(grid)

"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""
with open('day10_input.txt') as f:
    new_grid = np.array([[y for y in x] for x in [x.rstrip('\n') for x in f.readlines()]])
    
def print_path(path):
    for y in range(grid.shape[0]):
        row = ''
        for x in range(grid.shape[1]):
            if [y, x] in path:
                #row += grid[y][x]
                row += 'X'
                new_grid[y][x] = 'X'
            else:
                row += '.'
                new_grid[y][x] = '.'
        print(row)
        
    counter = 0    
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            if new_grid[y][x] == '.':
                x_left = 0
                i = x
                # calculate number of pipes from the left side - if number is odd then it is inside cell
                while i >= 0:
                    if (grid[y][i] == '|' or grid[y][i] == 'L' or grid[y][i] == 'J') and [y,i] in path:
                        x_left += 1
                    i -= 1
                if x_left % 2 == 1:
                    counter += 1
                    print(counter)
    
    print('answer is {}'.format(counter))

def move(curr, prev, path, length):
    
    path.append(curr)
    
    if grid[curr[0]][curr[1]] == '|':
        if curr[0] < prev[0] and curr[0] > 0:
            move([curr[0]-1, curr[1]], curr, path, length+1)
        if curr[0] > prev[0] and curr[0] < grid.shape[0]-1:
            move([curr[0]+1, curr[1]], curr, path, length+1)
    
    if grid[curr[0]][curr[1]] == '-':
        if curr[1] < prev[1] and curr[1] > 0:
            move([curr[0], curr[1]-1], curr, path, length+1)
        if curr[1] > prev[1] and curr[1] < grid.shape[1]-1:
            move([curr[0], curr[1]+1], curr, path, length+1)
    
    if grid[curr[0]][curr[1]] == 'L':
        if curr[0] > prev[0] and curr[1] < grid.shape[1]-1:
            move([curr[0], curr[1]+1], curr, path, length+1)
        if curr[1] < prev[1] and curr[0] > 0:
            move([curr[0]-1, curr[1]], curr, path, length+1)
    
    if grid[curr[0]][curr[1]] == 'J':
        if curr[0] > prev[0] and curr[1] > 0:
            move([curr[0], curr[1]-1], curr, path, length+1)
        if curr[1] > prev[1] and curr[0] > 0:
            move([curr[0]-1, curr[1]], curr, path, length+1)
            
    if grid[curr[0]][curr[1]] == '7':
        if curr[0] < prev[0] and curr[1] > 0:
            move([curr[0], curr[1]-1], curr, path, length+1)
        if curr[1] > prev[1] and curr[0] < grid.shape[0]-1:
            move([curr[0]+1, curr[1]], curr, path, length+1)
            
    if grid[curr[0]][curr[1]] == 'F':
        if curr[0] < prev[0] and curr[1] < grid.shape[1]-1:
            move([curr[0], curr[1]+1], curr, path, length+1)
        if curr[1] < prev[1] and curr[0] < grid.shape[0]-1:
            move([curr[0]+1, curr[1]], curr, path, length+1)
            
    if grid[curr[0]][curr[1]] == 'S':
        print('loop was finalized with length:{}'.format(length))
        print(path[0])
        print(path[1])
        print(path[-2])
        print(path[-1])
        grid[83][25] = '7'
        print_path(path)
        sys.exit()
        
        
if s_y > 0:
    move([s_y-1, s_x], [s_y, s_x], [[s_y, s_x]], 1)
if s_x < grid.shape[1]-1:
    move([s_y, s_x+1], [s_y, s_x], [[s_y, s_x]], 1)
if s_y < grid.shape[0]-1:
    move([s_y+1, s_x], [s_y, s_x], [[s_y, s_x]], 1)
if s_x > 0:
    move([s_y, s_x-1], [s_y, s_x], [[s_y, s_x]], 1)
            