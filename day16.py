with open('input16.txt') as file:
    data = file.readlines()
    data = [ line.strip() for line in data ]
    fields, tickets = [], []

    for line in data:
        if 'or' in line:
            fields.append(line)
        elif ',' in line:
            tickets.append(line)

def get_ranges():
    ranges = {}

    for line in fields:
        line = line.split(': ')
        field = line[0]

        line = line[1].split(' or ')
        A,B = line[0].split('-'), line[1].split('-')
        lower = (int(A[0]), int(A[1]))
        upper = (int(B[0]), int(B[1]))
        ranges[field] = (lower, upper)

    return ranges

def find_invalids():
    ranges = get_ranges()
    invalidNums = []
    validTickets = []

    for line in tickets:
        line = line.split(',')
        ticket = [int(num) for num in line]

        validTicket = True
        for num in ticket:
            validNum = False
            for f,r in ranges.items():
                a1,b1,a2,b2 = r[0][0], r[0][1], r[1][0], r[1][1]
                if num in range(a1,b1+1) or num in range(a2,b2+1):
                    validNum = True
                    break
            if not validNum:
                invalidNums.append(num)
                validTicket = False
        
        if validTicket:
            validTickets.append(ticket)

    return sum(invalidNums), validTickets

num, validTickets = find_invalids()
print(num)

def solve_fields():
    ranges = get_ranges()
    validCols = {}

    # find potention columns for each field
    for field, r in ranges.items():
        validCols[field] = []
        a1,b1,a2,b2 = r[0][0], r[0][1], r[1][0], r[1][1]

        for i in range(len(validTickets[0])):
            found = True
            for ticket in validTickets:
                num = ticket[i]
                if not (num in range(a1,b1+1) or num in range(a2,b2+1)):
                   found = False
                   break
            if found:
                validCols[field].append(i)

    # solve which column goes to which field
    solvedIndexes = []
    solvedFields = {}
    for i in range(len(fields)):
        for field, possibleCols in validCols.items():
            if len(possibleCols) == i+1:
                for j in possibleCols:
                    if j not in solvedIndexes:
                        solvedIndexes.append(j)
                        solvedFields[field] = j
                        break
                 
    # calculate answer
    total = 1
    for field, col in solvedFields.items():
        if 'departure' in field:
            total *= validTickets[0][col]

    return total

print(solve_fields())


