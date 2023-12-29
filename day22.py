with open('day22_input.txt') as f:
    parts = [[[int(b) for b in a.split(',')] for a in x.split('~')] for x in f.read().split('\n')]

# space - where blocks will be placed
space = {} 
parts = sorted(parts, key=lambda bs: min(b[2] for b in bs))

# adding piece into space
def add_piece(piece):
    [[x1, y1, z1], [x2, y2, z2]] = piece
    piece_count = 1 if space == {} else max(space.values()) + 1
    # place piece in the air
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            for z in range(z1 , z2+1):
                space[x, y, z] = piece_count         
    return piece_count

# drop the piece down to position            
def drop_piece(piece):
    global space
    blocks = [k for k, v in space.items() if v == piece]
    top = {}
    base = {}
    for x,y,z in blocks:
        top[x,y] = max([k[2] for k, v in space.items() if v != piece and k[0]==x and k[1]==y] + [0])
        base[x,y] = min(base[x,y], z) if (x,y) in base else z
    dz = min([base[x,y] - top[x,y] for x,y in top.keys()]) - 1
    for x,y,z in blocks:
        del space[x,y,z]
        space[x,y,z-dz] = piece
    

# getting pieces that are supporting the specified piece
def get_support_pieces(piece):
    below = []
    blocks = [k for k, v in space.items() if v == piece]
    for x, y, z in blocks:
        if (x, y, z-1) in space and (x, y, z-1) not in blocks and space[x, y, z-1] not in below:
            below.append(space[x, y, z-1])
    return below


# place and drop all the pieces
for p in parts:
    piece_no = add_piece(p)
    drop_piece(piece_no)

supports = {x: get_support_pieces(x) for x in set(space.values())}
answer1 = 0
answer2 = 0
for x in set(space.values()):
    # part 1 calculation
    if [x] not in [a for a in supports.values() if a!=[]]:
        answer1 +=1
    # part 2 calculation
    removed = set()
    to_remove = set([x])
    while to_remove:
        r = to_remove.pop()
        removed.add(r)
        # find pieces that are left without support piece once supports moved or were removed
        without_supports = [x for x in [k if [s for s in supp if s not in removed] == [] else None for k, supp in supports.items() if supp!=[]] if x!=None]
        for ws in without_supports:
            if ws not in removed and ws not in to_remove:
                answer2 += 1
                to_remove.add(ws)
print(answer1)
print(answer2)