import copy

with open('day23_input.txt') as f:
    # lists are overperformed by dictionaries
    grid = {(y,x): v for y, r in enumerate(f.read().split('\n')) for x, v in enumerate(r)}
       
# find start and end positions
start, end = min([k for k,v in grid.items() if v == '.']), max([k for k,v in grid.items() if v == '.'])

points = {start: [], end: []}
directions = [(1,0), (-1,0), (0,1), (0,-1)]

# find all road intersections in the grid and mark them *
for k, v in grid.items():
    if v != '#':
        c = 0
        y,x = k
        for dy, dx in directions:
            if (y+dy, x+dx) in grid and grid[y+dy, x+dx] != '#':
                c += 1
        if c > 2:
            points[k] = []
            
for y,x in points.keys():
    grid[y,x] = '*'
     
# find road segments, this later will be used for as graph edges
def findSegments(cell, path):
    if grid[cell] == '*' and len(path) > 1:
        points[path[0]].append([path[-1],len(path)-1])
        return
    y,x = cell
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    # ----- comment out this part for part2 -----
    # if grid[y,x] == '>': directions = [(0,1)]
    # elif grid[y,x] == 'v': directions = [(1,0)]
    # elif grid[y,x] == '<': directions = [(0,-1)]
    # elif grid[y,x] == '^': directions = [(-1,0)]
    # ----- end of block to be commented out -----
    for dy, dx in directions:
        if (y+dy, x+dx) in grid and grid[y+dy, x+dx] != '#' and (y+dy, x+dx) not in set(path):
            new_path = copy.deepcopy(path)
            new_path.append((y+dy, x+dx))
            findSegments((y+dy, x+dx), new_path)
   
for s in points:
    findSegments(s,[s])
    
    
# topological sort for nodes, ordering needed for longest path algorythm
stack, visited = [], {k: False for k in points.keys() }
def topologySort(p):
    global stack, visited, points
    visited[p] = True
    for next, l in points[p]:
        if (not visited[next]):
            topologySort(next)
    stack.append(p)
    
for p in points.keys():
	if (visited[p] == False):
		topologySort(p)


dist = {k:-1 for k in points.keys()}
dist[start] = 0

# finding longest path in directional graph
while len(stack) > 0:
    p = stack.pop()
    for next, l in points[p]:
        if dist[next] < dist[p] + l and next in stack:
            dist[next] = dist[p] + l
print('Longest path if using directional graph (works for first part):', dist[end])    
    
    
# brute force to find the longest path
paths = []
def findPath(point, path, length):
    if point == end:
        paths.append(length)
    for next in [e for e, l in points[point]]:
        if next not in path:
            new_path = copy.deepcopy(path)
            new_path.append(next)
            findPath(next, new_path, length+max([l for e, l in points[point] if e==next]))
            
findPath(start,[start], 0)
print('Longest path by bruteforcing:',max(paths))
