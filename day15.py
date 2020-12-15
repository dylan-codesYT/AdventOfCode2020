with open('input15.txt') as file:
    data = file.readlines()
    data = data[0].split(',')
    data = [ int(num) for num in data ]

def play_memory_game(size):
    mem = {}

    for i in range(len(data)-1):
        num = data[i]
        mem[num] = i

    for i in range(len(data)-1,size-1):
        num = data[i]

        if num not in mem:
            data.append(0)
            mem[num] = i

        else:
            j = mem[num]
            newNum = i - j
            data.append(newNum)
            mem[num] = i

    return data[-1]

print(play_memory_game(2020))
print(play_memory_game(30000000))
