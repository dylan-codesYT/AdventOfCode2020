with open('input25.txt') as file:
    data = file.readlines()
    cardKey = int( data[0].strip() )
    doorKey = int( data[1].strip() )

cardCount = 0
x = 1
while x != cardKey:
    cardCount += 1
    x = (x * 7) % 20201227

eKey = 1
for _ in range(cardCount):
    eKey = (eKey * doorKey) % 20201227

print(eKey)