# import input data to grid dictionary
with open('day21_input.txt') as f:
    grid = {(y,x): c for y, r in enumerate(f.read().split('\n')) for x, c in enumerate(r)}

y_max, x_max = max(grid)

# find starting position and replace it with 0 for zero steps
for y in range(y_max):
    for x in range(x_max):
        if grid[y,x] == 'S':
            grid[y,x] = '0'
            S_y, S_x = y, x

directions = [(1,0), (-1,0), (0,1), (0,-1)]

queue = [(S_y, S_x, 1)]
for step in range(1, 200):
    while len([1 for y, x, s in queue if s == step])>0:
        y, x, s = queue.pop(0)
        for dy, dx in directions:
            if (y+dy, x+dx) in grid:
                if grid[y+dy, x+dx] == '.':
                    grid[y+dy, x+dx] = str(step)
                    queue.append((y+dy, x+dx, step + 1))
                    
part1 = sum([1 for y in range(y_max+1) for x in range(x_max+1) if grid[y,x] not in ('.','#') and int(grid[y,x]) % 2 == 0 and int(grid[y,x]) <= 64])


# ----- Part 2 -----    

print(int(26501365 / 131), 26501365 % 131)
# we have 202300 full grids across and from start can reach both corners of left-most and right-most grids
# with every grid in each direction odd/even parity changes
# 26501365 is odd number of steps, so most center grid we need to take odd count
#
#     O
#    OEO
#   OEOEO
#    OEO
#     O
#
# steps = 131 * n + 65
# n = 0:           1 odd_full +   0 even_full -     1 odd_corners + 0 even_corners
# n = 1:           1 odd_full +   4 even_full +     1 odd_corners - 2 even_corners
# n = 2:           9 odd_full +   4 even_full -     3 odd_corners + 2 even_corners
# n = 3:           9 odd_full +  16 even_full +     3 odd_corners - 4 even_corners
# n = 4:          25 odd_full +  16 even_full -     5 odd_corners + 4 even_corners
# n = 2k:    (n+1)^2 odd_full + n^2 even_full - (n+1) odd_corners + n even_corners
                 
even_full = sum([1 for y in range(y_max+1) for x in range(x_max+1) if grid[y,x] not in ('.','#') and int(grid[y,x]) % 2 == 0])
odd_full = sum([1 for y in range(y_max+1) for x in range(x_max+1) if grid[y,x] not in ('.','#') and int(grid[y,x]) % 2 == 1])
even_corners = sum([1 for y in range(y_max+1) for x in range(x_max+1) if grid[y,x] not in ('.','#') and int(grid[y,x]) % 2 == 0 and int(grid[y,x]) > 65])
odd_corners = sum([1 for y in range(y_max+1) for x in range(x_max+1) if grid[y,x] not in ('.','#') and int(grid[y,x]) % 2 == 1 and int(grid[y,x]) > 65])

print(f'Answer to part one is {part1}')
print(f'Even full {even_full}')
print(f'Odd full {odd_full}')
print(f'Even corners {even_corners}')
print(f'Odd corners {odd_corners}')

def solve(n):
    return (n+1)**2 * odd_full + n**2 * even_full - (n+1) * odd_corners + n * even_corners
print('Answer to part two is', solve(202300))
