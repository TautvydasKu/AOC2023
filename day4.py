# import input data
with open('day4_input.txt') as f:
    input = [x.rstrip('\n') for x in f.readlines()]
    
# get left and right sides into two sets and intersect them to get repetitive numbers
cards = [x.replace('  ',' ').split(': ')[1].split(' | ') for x in input]
numbers = [set(x.split(' ')).intersection(set(y.split(' '))) for x, y in cards]
numbers2 = [2 ** (len(x)-1) for x in numbers if x != set()]
print('Answer to part one is: {}'.format(sum(numbers2)))



# create cards' count list and set every card to 1
counts = {k: 1 for k,v in list(enumerate(numbers, 1))}

# go from first card to last and add number of replicas won
for i, x in list(enumerate(numbers, 1)):
    for ii in range(1, len(x)+1):
        counts[i + ii] += counts[i]

print('Answer to part two is: {}'.format(sum([val for key, val in counts.items()])))