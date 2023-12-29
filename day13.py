# importing input data
with open('day13_input.txt') as f:
    input = [x.split('\n') for x in f.read().split('\n\n')]
    

# get differences number between rows
def diffRows(r1, r2):
    return sum([1 for i in range(len(r1)) if r1[i] != r2[i]])


# transpose grid making columns into rows
def gridT(x):
    return list(zip(*x))


# finding mirror
def findMir(x, part):
    for i in range(len(x)-1):
        if x[i] == x[i+1] or diffRows(x[i], x[i+1]) == 1:
            if isMirrored(x, i, part):
                return i
    return None


# checking if mirror is valid
def isMirrored(x, row, part):
    mirrored = True
    fixed = False
    i = 0
    while i <= row and i < len(x) - row - 1:
        if x[row - i] != x[row + 1 + i]:
            if not fixed and diffRows(x[row - i], x[row + 1 + i]) == 1:
                fixed = True
            else:
                mirrored = False
        i += 1
    if part == 1:
        # return true if rows are mirrored and there were no fixes
        return mirrored and not fixed
    else:
        # grid needs to be fixed necessarily and also mirrored with that fix for part2
        return mirrored and fixed


# run through both task parts and process the grids
for part in [1, 2]:
    answer = 0 
    for grid in input:
        r = findMir(grid, part)
        if r is not None:
            answer += (r+1) * 100
        else:
            # find column mirrors by transposing the grid
            answer += findMir(gridT(grid), part) + 1
    print('Answer to part {} is {}'.format(part, answer))