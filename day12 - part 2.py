# importing input data
with open('day12_input.txt') as f:
    input = [x.rstrip('\n').split(' ') for x in f.readlines()]
    
# part 2
input = [ [(('?'+x)*5)[1:], ((','+y)*5)[1:]] for x, y in input]    
input = [ [x, [int(z) for z in y.split(',')]] for x, y in input]

cache = {}

def f(row, groups, curr_pos, curr_group, curr_gr_len):
    
    # implementing caching to avoid calculating the same thing multiple times
    global cache
    key = (curr_pos, curr_group, curr_gr_len)
    # if new row was started to process then reset the cache
    if curr_pos == 0:
        cache = {}
    # if key in cache do not calculate it once again
    if key in cache:
        return cache[key]
    
    
    # check if row has ended
    if curr_pos == len(row):
        # check if all groups are finished that meet the condition or group there is n-1 groups finished and last one is needed length 
        if (curr_group == len(groups) and curr_gr_len == 0) or (curr_group == len(groups)-1 and curr_gr_len == groups[-1]):
            return 1
        else:
            return 0
    
    # if not in last position of the row, we continue
    to_return = 0
    # if current char is . either ? and we are not collecting a group move cursor(current position) forward
    if (row[curr_pos] == '.' or row[curr_pos] == '?') and curr_gr_len == 0:
        to_return += f(row, groups, curr_pos + 1, curr_group, curr_gr_len)
         
    # if current char is . either ? and we are collecting a group, check if we can open a new one if current one meets length criteria
    if (row[curr_pos] == '.' or row[curr_pos] == '?') and curr_group < len(groups) and curr_gr_len == groups[curr_group]:
        to_return += f(row, groups, curr_pos + 1, curr_group + 1, 0)
        
    # if current char is # or ? we can expand the group
    if(row[curr_pos] == '#' or row[curr_pos] == '?'):
        to_return += f(row, groups, curr_pos + 1, curr_group, curr_gr_len+1)
        
    cache[key] = to_return
    return to_return

results = [f(x, y, 0, 0, 0) for x, y in input]
print(sum(results))