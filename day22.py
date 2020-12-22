with open('input22.txt') as file:
    data = file.readlines()
    data = [ line.strip() for line in data ]

x = data.index('')
deck1 = [ int(data[i]) for i in range(x) if data[i].isdigit() ]
deck2 = [ int(data[i]) for i in range(x+1, len(data)) if data[i].isdigit() ]

# treat the decks as a queue
while len(deck1) != 0 and len(deck2) != 0:
    p1 = deck1.pop(0)
    p2 = deck2.pop(0)

    if p1 > p2:
        deck1.append(p1)
        deck1.append(p2)

    elif p2 > p1:
        deck2.append(p2)
        deck2.append(p1)

if len(deck1) == 0:
    winningDeck = deck2
else:
    winningDeck = deck1

count = 0
for i in range(len(winningDeck)):
    count += (i+1) * winningDeck[len(winningDeck) - 1 - i]
print(count)

# part2

def rec_combat(deck1, deck2) -> str:
    '''Return 'p1' or 'p2', depending on who wins'''
    prevRounds = []

    while len(deck1) != 0 and len(deck2) != 0:
        if (deck1, deck2) in prevRounds:
            return 'p1'
        else:
            prevRounds.append((deck1.copy(), deck2.copy()))

            p1 = deck1.pop(0)
            p2 = deck2.pop(0)

            # determine winner with a sub game
            if len(deck1) >= p1 and len(deck2) >= p2:
                winner = rec_combat(deck1.copy()[:p1], deck2.copy()[:p2])

                if winner == 'p1':
                    deck1.append(p1)
                    deck1.append(p2)
                else:
                    deck2.append(p2)
                    deck2.append(p1)

            # determine winner by card value
            else:
                if p1 > p2:
                    deck1.append(p1)
                    deck1.append(p2)
                elif p2 > p1:
                    deck2.append(p2)
                    deck2.append(p1)

    if len(deck1) == 0:
        return 'p2'
    else:
        return 'p1'

deck1 = [ int(data[i]) for i in range(x) if data[i].isdigit() ]
deck2 = [ int(data[i]) for i in range(x+1, len(data)) if data[i].isdigit() ]

winner = rec_combat(deck1, deck2)
if winner == 'p1':
    winningDeck = deck1
else:
    winningDeck = deck2

count = 0
for i in range(len(winningDeck)):
    count += (i+1) * winningDeck[len(winningDeck) - 1 - i]
print(count)