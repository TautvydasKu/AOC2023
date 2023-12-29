import math

# importing input data
with open('day20_input.txt') as f:
    input = [x.strip('\n') for x in f.readlines()]

# modules contains parced input, states contain states for module, queue is maintained for processing
modules = {}
states = {}
queue = []

# part 1 - interested in number of lows and highs after 1000 cycles
# part 2 - we need to find loops so trying out 10000 cycles
for part in [1,2]:
    # parse input to fill in modules and initial states
    for r in input:
        name, send_to = r.split(' -> ')
        if name == 'broadcaster':
            modules['broadcaster'] = ['b', send_to.split(', ')]
        else:
            modules[name[1:]] = [name[0], send_to.split(', ')]
            if name[0] == '%':
                states[name[1:]] = 'low'
            else:
                states[name[1:]] = {}
    for r in input:
        name, send_to = r.split(' -> ')
        for s in send_to.split(', '):
            if s in [k for k, v in modules.items() if v[0] == '&']:
                states[s][name[1:]] = 'low'
    
    received = []
    for i in range(1000 if part == 1 else 10000):
        queue.append(['broadcaster', 'low', 'button'])
        while queue:
            name, state, prev = queue.pop(0)
            received.append([i,name,state,prev])
            # if name not in modules then do not need to process further
            if name not in modules.keys():
                continue
            type, send_to = modules[name]
            # handle broadcaster module
            if type == 'b':
                for s in send_to:
                    queue.append([s, state, name])
            # handle inverter / flip-flop module
            if type == '%':
                if state == 'low':
                    states[name] = 'high' if states[name] == 'low' else 'low'
                    for s in send_to:
                        queue.append([s, states[name], name])
            # handle conjuction module
            if type == '&':
                states[name][prev] = state
                if len([x for x in states[name].values() if x == 'low']) == 0:
                    pulse = 'low'
                else:
                    pulse = 'high'
                for s in send_to:
                    queue.append([s, pulse, name])
    if part == 1:                    
        print('Answer for part one is {}'.format(sum([1 for i,n,s,p in received if s == 'high']) * \
                                                 sum([1 for i,n,s,p in received if s == 'low']))) 
    else:
        for i,n,s,p in received:
            # gh needs to receive all highs at once to send low to rx
            if n == 'gh' and s == 'high':
                print(f'on cycle {i+1} {n} got high from {p}')
        # found loops for all 4 - answer will be least common multiplier
        print('Answer for part two is {}'.format(math.lcm(3733, 3793, 3947, 4057)))