# importing input data
with open('day15_input.txt') as f:
    input = [x for x in f.read().strip('\n').split(',')]
    
# hashing function
def hsh(x):
    value = 0
    for c in x:
        value = ((value + ord(c)) * 17) % 256
    return value
        
# part 1
result = [hsh(x) for x in input]
print('Answer to part one is {}'.format(sum(result)))
        
# part 2
boxes = [dict() for i in range(256)]
for step in input:
    if step.find("=") > 0:
        # replace or insert lens
        op, fl = step.split("=")
        box = hsh(op)
        boxes[box][op] = fl
    if step.find("-") > 0:
        # remove lens
        op = step[:-1]
        box = hsh(op)
        if op in boxes[box]:
            boxes[box].pop(op)

answer = 0
for b, box in list(enumerate(boxes, 1)):
    for i, f in list(enumerate([int(v) for k, v in box.items()] , 1)):
        answer += b * i * f
print('Answer to part two is {}'.format(answer))