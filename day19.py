import copy, math

# import and parse the input
with open('day19_input.txt') as f:
    workflows, parts = [[y for y in x.split('\n')] for x in f.read().split('\n\n')]
workflows = { x.split('{')[0]: [y for y in x.split('{')[1][:-1].split(',')] for x in workflows }
mapping = {'x':0, 'm': 1, 'a': 2, 's': 3}

for task in [1, 2]:
    if task == 1:
        # for task one each part is described as range of exactly one point in 4 dimension plain
        q = []
        for p in parts:
            p = [[int(x), int(x)] for x in p[1:-1].replace('x=','').replace('m=','').replace('a=','').replace('s=','').split(',')]
            q.append(['in', 0, p])
    else:
        # for part two we input whole 4 dimension plain
        q = [['in', 0, [[1,4000], [1,4000], [1,4000], [1,4000]]]]

    accepted = []
    while len(q) > 0:
        wf, step, ranges = q.pop()
        
        # if workflow/state is A or R, collect accepted and do nothing for rejected
        if wf == 'A':
            accepted.append(ranges)
            continue
        if wf == 'R':
            continue
        curr = workflows[wf][step]
        
        # process workflow for instruction greater than
        if curr.find('>') > 0:
            r = mapping[curr.split('>')[0]]
            cut = int(curr.split('>')[1].split(':')[0])
            new_wf = curr.split('>')[1].split(':')[1]
            if ranges[r][0] < cut:
                new_ranges = copy.deepcopy(ranges)
                new_ranges[r][1] = min(new_ranges[r][1], cut) 
                q.append([wf, step + 1, new_ranges])
            if ranges[r][1] >= cut:
                new_ranges = copy.deepcopy(ranges)
                new_ranges[r][0] = max(cut + 1, new_ranges[r][0]) 
                q.append([new_wf, 0, new_ranges])

        # process workflow for instruction less than
        elif curr.find('<') > 0:
            r = mapping[curr.split('<')[0]]
            cut = int(curr.split('<')[1].split(':')[0])
            new_wf = curr.split('<')[1].split(':')[1]
            if ranges[r][0] < cut:
                new_ranges = copy.deepcopy(ranges)
                new_ranges[r][1] = min(new_ranges[r][1], cut-1) 
                q.append([new_wf, 0, new_ranges])
            if ranges[r][1] >= cut:
                new_ranges = copy.deepcopy(ranges)
                new_ranges[r][0] = max(cut, new_ranges[r][0]) 
                q.append([wf, step + 1, new_ranges])
                
        # move to new workflow if there is no comparison in current workflow
        else:
            q.append([curr, 0, ranges])
        
    if task == 1:
        print('Answer for part 1 is {}'.format(sum([sum([y[0] for y in x]) for x in accepted])))
    else:
        print('Answer for part 2 is {}'.format((sum([math.prod([y[1]-y[0]+1 for y in x]) for x in accepted]))))