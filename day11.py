with open('input11.txt') as file:
    data = file.readlines()
    data = [ list(line.strip()) for line in data ]
    original = data.copy()

def get_num_occupied():
    count = 0
    for row in data:
        for seat in row:
            if seat == '#':
                count +=1
    return count

def get_adjacent_count(row,col):
    count = 0
    currentRow = data[row]

    #check left
    if col-1 >= 0:
        if currentRow[col-1] == '#': count +=1

    # check right
    if col+1 <= len(currentRow)-1:
        if currentRow[col+1] == '#': count += 1

    # above
    if row-1 >= 0:
        aboveRow = data[row-1]
        if aboveRow[col] == '#':
            count+=1
        
        if col-1 >= 0:
            if aboveRow[col-1] == '#':
                count+=1
        
        if col+1 <= len(aboveRow)-1:
            if aboveRow[col+1] == '#':
                count+=1

    # below
    if row+1 <= len(data)-1:
        belowRow = data[row+1]
        if belowRow[col] == '#':
            count+=1
        
        if col-1 >= 0:
            if belowRow[col-1] == '#':
                count+=1
        
        if col+1 <= len(belowRow)-1:
            if belowRow[col+1] == '#':
                count+=1
    
    return count

def get_adjaccent_count_p2(row, col):
    count = 0

    # i is for row, j for col
    iU, iD, jR, jL = row-1, row+1, col+1, col-1
    N, S, E, W, NE, SE, NW, SW = False, False, False, False, False, False, False, False

    while not (N and S and W and E and NE and SE and NW and SW):
        # North
        if not N and iU >= 0:
            if data[iU][col] == '#':
                count+=1
                N=True
            elif data[iU][col] == 'L':
                N=True
        else:
            N=True
            
        # South
        if not S and iD <= len(data)-1:
            if data[iD][col] == '#':
                count+=1
                S=True
            elif data[iD][col] == 'L':
                S=True
        else:
            S=True

        # East
        if not E and jR <= len(data[row])-1:
            if data[row][jR] == '#':
                count+=1
                E=True
            elif data[row][jR] == 'L':
                E=True
        else:
            E=True

        # West
        if not W and jL >= 0:
            if data[row][jL] == '#':
                count+=1
                W=True
            elif data[row][jL] == 'L':
                W=True
        else:
            W=True

        # North West
        if not NW and iU >= 0 and jL >= 0:
            if data[iU][jL] == '#':
                count+=1
                NW=True
            elif data[iU][jL] == 'L':
                NW=True
        else:
            NW=True

        # South West
        if not SW and iD <= len(data)-1 and jL >= 0:
            if data[iD][jL] == '#':
                count+=1
                SW=True
            elif data[iD][jL] == 'L':
                SW=True
        else:
            SW=True

        # North East
        if not NE and iU >= 0 and jR <= len(data[row])-1:
            if data[iU][jR] == '#':
                count+=1
                NE=True
            elif data[iU][jR] == 'L':
                NE=True
        else:
            NE=True

        # South East
        if not SE and iD <= len(data)-1 and jR <= len(data[row])-1:
            if data[iD][jR] == '#':
                count+=1
                SE=True
            elif data[iD][jR] == 'L':
                SE=True
        else:
            SE=True

        iU -= 1
        iD += 1
        jR += 1
        jL -= 1

    return count
        

def run_rules(tolerance):
    newSeating = []

    for row in range(len(data)):
        currentRow = data[row]
        newRow = []

        for col in range(len(currentRow)):
            if currentRow[col] == '.':
                newRow.append('.')
                continue

            adjacentCount = 0
            if tolerance == 4:
                adjacentCount = get_adjacent_count(row,col)
            elif tolerance == 5:
                adjacentCount = get_adjaccent_count_p2(row,col)

            if currentRow[col] == 'L' and adjacentCount == 0:
                newRow.append('#')
            
            elif currentRow[col] == '#' and adjacentCount >= tolerance:
                newRow.append('L')

            else:
                newRow.append(currentRow[col])
        newSeating.append(newRow)

    for i in range(len(data)):
        data[i] = newSeating[i]

def get_final_count(tolerance):
    prev = data.copy()
    run_rules(tolerance)

    while data != prev:
        prev = data.copy()
        run_rules(tolerance)
    
    return get_num_occupied()

print(get_final_count(4))

# part 2
data = original.copy()
print(get_final_count(5))