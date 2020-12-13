
with open('input13.txt') as file:
    data = file.readlines()
    data = [ line.strip() for line in data ]
    data[1] = data[1].split(',')

def get_id_minutes():
    arrival = int(data[0])
    ids = data[1]

    lowest = 99999999999999
    lowID = 0
    for item in ids:
        if item != 'x':
            id = int(item)
        else:
            continue

        idMultiple = arrival // id
        difference = (id * (idMultiple+1)) - arrival
        if difference < lowest:
            lowest = difference
            lowID = id

    return lowID * lowest

print(get_id_minutes())

# part two

def mod_inverse(a,n):
    # find some x such that (a*x) % n == 1
    a = a % n
    if n == 1:
        return 1
    for x in range(1, n):
        if (a*x) % n == 1:
            return x
    
# n busses
# bus k at index i departs at a time t+i
# t+i % k == 0
# t % k == -i
# t % k = k-i
# index = (k - (i%k)) % k
def get_earliest_time():
    ids = []
    fullProduct = 1
    for i in range(len(data[1])):
        item = data[1][i]
        if item != 'x':
            k = int(item)
            i = i % k
            ids.append(((k-i)%k,k))
            fullProduct *= k

    total = 0
    for i,k in ids:
        partialProduct = fullProduct // k

        inverse = mod_inverse(partialProduct,k)
        assert (inverse * partialProduct) % k == 1

        term = inverse * partialProduct * i
        total += term

    return total % fullProduct


print(get_earliest_time())