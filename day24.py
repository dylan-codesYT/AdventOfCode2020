with open('input24.txt') as file:
    data = file.readlines()
    data = [ line.strip() for line in data ]

def parse(line):
    dirs = []

    while len(line) > 0:
        if line[0] in ['w', 'e']:
            dirs.append(line[0])
            line = line[1:]
        else:
            dirs.append(line[:2])
            line = line[2:]
    return dirs

lines = [ parse(line) for line in data ]
blackTiles = set()

for line in lines:
    # x,y,z and the center is at 0,0,0
    # e,w: xy-plane
    # nw,se: xz-plane
    # ne,sw: yz-plane

    x,y,z = 0,0,0
    for dir in line:
        # xy-axis
        if dir == 'w':
            x += 1
            y -= 1
        elif dir == 'e':
            x -= 1
            y += 1

        # xz-axis
        elif dir == 'nw':
            x += 1
            z -= 1
        elif dir == 'se':
            x -= 1
            z += 1
        
        # yz-axis
        elif dir == 'ne':
            y += 1
            z -= 1
        elif dir == 'sw':
            y -= 1
            z += 1
    
    if (x,y,z) in blackTiles:
        blackTiles.remove((x,y,z))
    else:
        blackTiles.add((x,y,z))

print(len(blackTiles))

# part 2

def get_adjacent_count(tile):
    (x,y,z) = tile
    count = 0
    for (i,j,k) in [(1,-1,0), (-1,1,0), (1,0,-1), (-1,0,1), (0,1,-1), (0,-1,1)]:
        if (x+i, y+j, z+k) in blackTiles:
            count += 1
    return count

for _ in range(100):
    newBlackTiles = set()
    adjacentTiles = set()

    # find all adjacent tiles
    for (x,y,z) in blackTiles:
        count = get_adjacent_count((x,y,z))
        if count==1 or count==2:
            newBlackTiles.add((x,y,z))
        
        for (i,j,k) in [(1,-1,0), (-1,1,0), (1,0,-1), (-1,0,1), (0,1,-1), (0,-1,1)]:
            adjacentTiles.add((x+i, y+j, z+k))
    
    # find the adjacent tiles that should be flipped
    for (x,y,z) in adjacentTiles:
        count = get_adjacent_count((x,y,z))
        if (x,y,z) in blackTiles and (count==1 or count==2):
            newBlackTiles.add((x,y,z))
        elif (x,y,z) not in blackTiles and count==2:
            newBlackTiles.add((x,y,z))

    blackTiles = newBlackTiles

print(len(blackTiles))
