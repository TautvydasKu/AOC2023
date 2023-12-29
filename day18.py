# import input data
with open('day18_input.txt') as f:
    input = [[d, int(l), c[1:-1]] for x in f.readlines() for d, l, c in [x.strip('\n').split(' ')]]

moves = {'R': (0,1), 'D': (1,0), 'L': (0,-1), 'U': (-1,0)}
int_to_moves = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}

for part in [1,2]:
    inp = list(input)
    if part == 2:
        inp = [[int_to_moves[c[-1]], int(c[1:-1], 16), '-'] for d, l, c in input]
    y, x = 0, 0
    apexes = []
    for d, l, c in inp:
        y += l * moves[d][0]
        x += l * moves[d][1]
        apexes.append((y, x))
    
    # shoelace formula for inner area + perimeter / 2 + 1 to account for edges area
    answer = 0
    for i in range(len(apexes)-1):
        answer += apexes[i][1] * apexes[i+1][0] - apexes[i+1][1] * apexes[i][0]
    answer = int(answer / 2 + sum([l for d, l, c in inp]) / 2 + 1)
    print('Answer for part {} is {}'.format(part,answer))