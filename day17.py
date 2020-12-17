with open('input17.txt') as file:
    data = file.readlines()
    data = [ line.strip() for line in data ]

def get_initial_active_points(fourDimensions:bool):
    activePoints = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] =='#':
                if not fourDimensions:
                    activePoints.add((i,j,0))
                else:
                    activePoints.add((i,j,0,0))
    return activePoints

# part one
activePoints = get_initial_active_points(False)
for r in range(6):
    newActivePoints = set()

    # check each x,y,z point
    for x in range(-10-r,r+10):
        for y in range(-10-r, r+10):
            for z in range(-2-r, r+2):

                # for the current x,y,z, check the neighbors
                activeCount = 0
                for i in range(-1,2):
                    for j in range(-1,2):
                        for k in range(-1,2):
                            if not (i==0 and k==0 and j==0):
                                if (x+i, y+j, z+k) in activePoints:
                                    activeCount += 1
                
                # apply rules
                if (x,y,z) in activePoints and (activeCount == 2 or activeCount == 3):
                    newActivePoints.add((x,y,z))
                if (x,y,z) not in activePoints and activeCount == 3:
                    newActivePoints.add((x,y,z))

    activePoints = newActivePoints

print(len(activePoints))

# part 2
activePoints = get_initial_active_points(True)
for r in range(6):
    newActivePoints = set()

    # check each x,y,z point
    for x in range(-10-r,r+10):
        for y in range(-10-r, r+10):
            for z in range(-2-r, r+2):
                for w in range(-2-r, r+2):

                    # for the current x,y,z,w check the neighbors
                    activeCount = 0
                    for i in range(-1,2):
                        for j in range(-1,2):
                            for k in range(-1,2):
                                for p in range(-1,2):
                                    if not (i==0 and k==0 and j==0 and p==0):
                                        if (x+i, y+j, z+k, w+p) in activePoints:
                                            activeCount += 1
                
                    # apply rules
                    if (x,y,z,w) in activePoints and (activeCount == 2 or activeCount == 3):
                        newActivePoints.add((x,y,z,w))
                    if (x,y,z,w) not in activePoints and activeCount == 3:
                        newActivePoints.add((x,y,z,w))

    activePoints = newActivePoints
    print(len(activePoints))

print(len(activePoints))

