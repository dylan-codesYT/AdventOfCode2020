
with open('input12.txt') as file:
    data = file.readlines()
    data = [ line.strip() for line in data]

def get_displacement():
    x,y = 0,0

    # dirs: N=0, E=1, S=2, W=3
    dir = 1

    for line in data:
        cmd, value = line[0], int(line[1:])

        if cmd == 'N' or (dir==0 and cmd=='F'):
            y += value

        elif cmd == 'S' or (dir==2 and cmd=='F'):
            y -= value

        elif cmd == 'E' or (dir==1 and cmd=='F'):
            x += value

        elif cmd == 'W' or (dir==3 and cmd=='F'):
            x -= value

        elif cmd == 'R':
            dir += value // 90
            dir = dir % 4

        elif cmd == 'L':
            dir -= value // 90
            dir = dir %4

    return abs(x) + abs(y)

print(get_displacement())

# part 2
def get_distance_with_waypoint():
    x,y = 0,0
    i,j = 10,1

    for line in data:
        cmd, value = line[0], int(line[1:])

        if cmd == 'N':
            j += value
        elif cmd == 'S':
            j -= value
        elif cmd == 'E':
            i += value
        elif cmd == 'W':
            i -= value

        elif cmd == 'R':
            while value > 0:
                i1 = j
                j1 = -1 * i
                i,j = i1, j1
                value -= 90
        
        elif cmd == 'L':
            while value > 0:
                i1 = -1 * j
                j1 = i
                i,j = i1, j1
                value-=90

        elif cmd == 'F':
            x += value * i
            y += value * j

    return abs(x) + abs(y)

print(get_distance_with_waypoint())
            
