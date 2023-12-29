import numpy as np

with open('day16_input.txt') as f:
    grid = np.array([[y for y in x] for x in [x.rstrip('\n') for x in f.readlines()]])

def energize(beams):
    visited = [[{'t': 0, 'r': 0, 'b': 0, 'l': 0} for x in range(grid.shape[1])] for y in range(grid.shape[0])]
    while len(beams) > 0:
        for y_curr, x_curr, y_prev, x_prev in beams:
            beams.remove([y_curr, x_curr, y_prev, x_prev])
            # skip beam if out of range
            if y_curr < 0 or x_curr <0 or y_curr >= grid.shape[0] or x_curr >= grid.shape[1]:
                continue
            
            # checking entry direction
            if x_curr > x_prev:
                # entered from left
                direction = 'l'
            if x_curr < x_prev:
                # entered from right
                direction = 'r'
            if y_curr > y_prev:
                # entered from top
                direction = 't'
            if y_curr < y_prev:
                # entered from bottom
                direction = 'b'
    
            if visited[y_curr][x_curr][direction] == 0:
                # cell not entered from the same direction already
                visited[y_curr][x_curr][direction] = 1
                if grid[y_curr][x_curr] == '.':
                    beams.append([y_curr + (y_curr - y_prev), x_curr + (x_curr - x_prev), y_curr, x_curr])
                if grid[y_curr][x_curr] == '|':
                    if direction == 'l' or direction == 'r':
                        beams.append([y_curr + 1, x_curr, y_curr, x_curr])
                        beams.append([y_curr - 1, x_curr, y_curr, x_curr])
                    else:
                        beams.append([y_curr + (y_curr - y_prev), x_curr, y_curr, x_curr])
                if grid[y_curr][x_curr] == '-':
                    if direction == 't' or direction == 'b':
                        beams.append([y_curr, x_curr + 1, y_curr, x_curr])
                        beams.append([y_curr, x_curr - 1, y_curr, x_curr])
                    else:
                        beams.append([y_curr, x_curr + (x_curr - x_prev), y_curr, x_curr])
                if grid[y_curr][x_curr] == '\\':
                    beams.append([y_curr + (x_curr - x_prev), x_curr + (y_curr - y_prev), y_curr, x_curr])
                if grid[y_curr][x_curr] == '/':
                    beams.append([y_curr - (x_curr - x_prev), x_curr - (y_curr - y_prev), y_curr, x_curr])
                        
    visited = [[max(x.values()) for x in y] for y in visited]    
    return sum([sum(x) for x in visited])
    

# Part 1
# beams structure [y_curr, x_curr, y_prev, x_prev]
beams = [[0, 0, 0, -1]]
print('Answer to Part 1 is {}'. format(energize(beams)))

# Part 2
beams = []
beams += [ [y, 0, y, -1] for y in range(grid.shape[0])]
beams += [ [y, grid.shape[1]-1, y, grid.shape[1]] for y in range(grid.shape[0])]
beams += [ [0, x, -1, x] for x in range(grid.shape[1])]
beams += [ [grid.shape[0]-1, x, grid.shape[0], x] for x in range(grid.shape[1])]
print('Answer to Part 2 is {}'. format(max([energize([x]) for x in beams])))