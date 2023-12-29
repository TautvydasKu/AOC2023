# import the input data
with open('day9_input.txt') as f:
    input = [[int(x) for x in x.rstrip('\n').split()] for x in f.readlines()]
    
def extrapolate(seq, part):
    # build a tree downwards
    rows = [list(seq)]
    while sum([abs(x) for x in rows[-1]]) > 0:
        new_row = []
        for i in range(len(rows[-1])-1):
            new_row.append(rows[-1][i+1] - rows[-1][i])
        rows.append(new_row)
        
    if part == 1:
        # summing right most digits
        return sum([x[-1] for x in rows])
    else:
        # summing left most digits, sign is altering with each row
        return sum([r[0] * (-1) ** i for i, r in list(enumerate(rows))])
    
print('Answer to part one is {}'.format(sum([extrapolate(x, 1) for x in input])))
print('Answer to part two is {}'.format(sum([extrapolate(x, 2) for x in input])))