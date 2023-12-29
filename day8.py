import math

# import the input data
with open('day8_input.txt') as f:
    moves = f.readline().rstrip()
    f.readline()
    map_list = [x.rstrip('\n').replace(' = (',' ').replace(',','').replace(')','').split() for x in f.readlines()]
    map = dict([[x, [y, z]]for x, y, z in map_list])


# ---------- part 1 ----------
pos = 'AAA'
target = 'ZZZ'
moving = True
move = 0
counter = 0

while moving:
    counter += 1
    if moves[move] == 'L':
        pos = map[pos][0]
    else:
        pos = map[pos][1]
    move = (move + 1) % len(moves)
    if pos == target:
        moving = False
print('Answer to part one is: {}'.format(counter))



# ---------- part 2 ----------
# nodes to start
pos = [x for x,y,z in map_list if x[2] == 'A']

repeats = []

for node in pos:
    curr_pos = node
    moving = True
    move = 0
    counter = 0
    prev_counter = 0
    findings = []
    # loop from each starting node and collect 20 final position (as it's a loop)
    while moving:
        counter += 1
        if moves[move] == 'L':
            curr_pos = map[curr_pos][0]
        else:
            curr_pos = map[curr_pos][1]
        move = (move + 1) % len(moves)
        if curr_pos[2] == 'Z':
            findings.append([counter, curr_pos, counter - prev_counter])
            prev_counter = counter
        if len(findings) > 20:
            moving = False
            print(findings)
    # each starting node path has a loop, take the length of that loop
    repeats.append(findings[-1][2])
    
# find the answer by using least common multiplier
print('Answer to part two is: {}'.format(math.lcm(*repeats)))
