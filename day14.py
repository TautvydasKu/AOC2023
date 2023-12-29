# importing input data
with open('day14_input.txt') as f:
    input = [x.rstrip('\n') for x in f.readlines()]

# transpose function
def t(input):
    return [''.join(i for i in x) for x in list(zip(*input))]

# rotate -90 deg x times
def rotate(input, times):
    inp = list(input)
    for i in range(times):
        inp = [''.join(i for i in x) for x in list(zip(*inp))[::-1]]
    return inp

# counter for load
def counter(platform):
    answer = 0
    for i, row in list(enumerate(platform)):
        answer += (len(platform) - i) * sum([1 for x in row if x == 'O'])
    return answer

# perform tilt operation
def tilt(input):
    tilted = []
    for col in input:
        new_col = ''
        cnt_o = 0
        cnt_d = 0
        for i in range(len(col)):
            if col[i] == 'O':
                cnt_o += 1
            if col[i] == '.':
                cnt_d += 1
            if col[i] == '#':
                new_col += 'O' * cnt_o + '.' * cnt_d + '#'
                cnt_o = 0
                cnt_d = 0
        if cnt_o > 0 or cnt_d > 0:
            new_col += 'O' * cnt_o + '.' * cnt_d
        tilted.append(new_col)
    return tilted
   

platform = list(input)
# part 2 cycle
for i in range(1000):
    prev = list(platform)
    # one full cycle
    platform = rotate(tilt(rotate(tilt(rotate(tilt(rotate(tilt(rotate(platform, 1)), 3)), 3)), 3)), 2)
    print('after {} cycles load is {}'.format(i+1, counter(platform)))

# found repetition loop of 11 after 1000 cycles
# (1000000000-1000) % 11 = 0, meaning the answer after 1000000000 cycles will be the same as after 1000


# part 1
platform = rotate(tilt(rotate(input, 1)), 3)
print('Answer for part one was {}'.format(counter(platform)))       
