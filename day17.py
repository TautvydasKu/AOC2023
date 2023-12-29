import heapq

with open('day17_input.txt') as f:
    # lists are overperformed by dictionaries
    grid = {(y,x): int(h) for y, r in enumerate(f.read().split('\n')) for x, h in enumerate(r)}

# modified dijkstra to find the path
def path(start, end, min_blocks, max_blocks):
    heap = [(0, *start , 0, 0)]
    visited = set() # drastic speed improvement changing list into set
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    while len(heap) > 0:
        # take minimum from heap
        heat, y, x, py, px = heapq.heappop(heap)
        # if reached final destination return heat
        if (y, x) == end:
            return heat
        # if already visited do not process further
        if (y, x, py, px) in visited:
            continue
        # add to visited and add new point to visit
        visited.add((y, x, py, px))
        for dy, dx in [d for d in directions if d not in [(py, px), (-py, -px)]]:
            new_heat, new_y, new_x = heat, y, x
            for i in range(1, max_blocks+1):
                new_y += dy
                new_x += dx
                if (new_y, new_x) not in grid:
                    break
                new_heat += grid[new_y, new_x]
                if i>= min_blocks:
                    heapq.heappush(heap, (new_heat, new_y, new_x, dy, dx))
            
print('Answer to part 1 is {}'.format(path((0,0), max(grid), 1, 1000)))
print('Answer to part 2 is {}'.format(path((0,0), max(grid), 4, 10)))