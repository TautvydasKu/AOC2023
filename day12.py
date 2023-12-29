import itertools

# importing input data
with open('day12_input.txt') as f:
    input = [x.rstrip('\n').split(' ') for x in f.readlines()]
    
answer1 = 0     
for row, numbers in input:
    max_hash = sum([int(x) for x in numbers.split(',')])
    curr_hash = len([x for x in row if x == '#'])
    unknown_pos = [i for i, x in list(enumerate(row)) if x == '?']
    
    combinations = []
    # generate all possible combinations using remaining symbols
    for positions in list(itertools.combinations(unknown_pos, max_hash-curr_hash)):
        new_row = row
        for pos in positions:
            new_row = new_row[:pos] + '#' + new_row[pos+1:]
        new_row = new_row.replace('?','.')
        combinations.append(new_row)
        
    # check with combinations matches the partern
    valid_combinations = [comb for comb in combinations if ''.join(',' + str(len(x)) for x in comb.split('.') if x != '')[1:] == numbers]
    answer1 += len(valid_combinations)
    
print(answer1)   