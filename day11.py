import numpy as np

# importing input data
with open('day11_input.txt') as f:
    input = [x.rstrip('\n') for x in f.readlines()]
    
# find empty rows
rows = []
for i, r in list(enumerate(input)):
    if r.replace('.','') == '':
        rows.append(i)

# transpose input and find empty columns
input_t = [''.join(i for i in x) for x in np.transpose(np.array([[y for y in x] for x in input])).tolist()]
cols = []
for i, r in list(enumerate(input_t)):
    if r.replace('.','') == '':
        cols.append(i)

# find galaxies' locations
galaxies = []
for y, r in list(enumerate(input)):
    for x in range(len(r)):
        if(r[x] == '#'):
            galaxies.append([y, x])

# count distances
sum1 = 0
sum2 = 0
for i, g in list(enumerate(galaxies)):
    for ii in range(i+1, len(galaxies)):
        diff = abs(g[0]- galaxies[ii][0]) + abs(g[1]- galaxies[ii][1])
        
        # count empty rows/columns as double, add one for each duplicate
        diff1 = diff + len([x for x in cols if x > min(g[1], galaxies[ii][1]) and x < max(g[1], galaxies[ii][1])])
        diff1 += len([x for x in rows if x > min(g[0], galaxies[ii][0]) and x < max(g[0], galaxies[ii][0])])
        sum1 += diff1
        
        # count empty rows/columns as 1 000 000, add 999 999 for each duplicate
        diff2 = diff + len([x for x in cols if x > min(g[1], galaxies[ii][1]) and x < max(g[1], galaxies[ii][1])]) * 999999
        diff2 += len([x for x in rows if x > min(g[0], galaxies[ii][0]) and x < max(g[0], galaxies[ii][0])]) * 999999
        sum2 += diff2
        
print('Answer to part one is: {}'.format(sum1))
print('Answer to part two is: {}'.format(sum2))