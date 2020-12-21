with open('input21.txt') as file:
    data = file.readlines()
    data = [ line.strip() for line in data ]

foods = []
for food in data:
    x = food.index('contains')

    ingrients = food[:x-1].split()
    allergens = food[x+9:-1].split(', ')
    foods.append((ingrients, allergens))

solved = {}
unsolved = {}
for i in range(len(foods)):
    if len(foods[i][1]) == 1:
        curr = foods[i][1][0]

        if curr not in solved:
            indxs = []
            for j in range(len(foods)):
                if curr in foods[j][1] and i != j:
                    indxs.append(j)

            possible = foods[i][0]
            for k in indxs:
                combined = []
                I = foods[k][0]
                for f in I:
                    if f in possible:
                        combined.append(f)
                possible = combined.copy()

            if len(possible) == 1:
                solved[curr] = possible[0]
            else:
                unsolved[curr] = possible.copy()

while len(unsolved) > 0:
    stillUnsolved = {}

    for key in unsolved.keys():
        possible = []

        for value in unsolved[key]:
            if value not in solved.values():
                possible.append(value)

        if len(possible) == 1:
            solved[key] = possible[0]
        else:
            stillUnsolved[key] = possible

    unsolved = stillUnsolved

count = 0
for ingredients, allergens in foods:
    for i in ingredients:
        if i not in solved.values():
            count += 1

print(count)

# part 2
badIngredients = []
for i in solved.keys():
    badIngredients.append(i)
badIngredients.sort()

canonical = ''
for i in badIngredients:
    canonical += solved[i] + ','
print(canonical[:-1])

