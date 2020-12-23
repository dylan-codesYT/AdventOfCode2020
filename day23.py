with open('input23.txt') as file:
    data = file.readlines()
    data = [ line.strip() for line in data ]
    data = [ int(x) for x in data[0] ]

cups = data.copy()
currCup = cups[0]
for _ in range(100):
    # pickup 3 cups
    x = cups.index(currCup)
    cup1 = cups.pop((x+1)%len(cups))

    x = cups.index(currCup)
    cup2 = cups.pop((x+1)%len(cups))

    x = cups.index(currCup)
    cup3 = cups.pop((x+1)%len(cups))

    # find destination
    if currCup == 1:
        destination = 9
    else:
        destination = currCup - 1

    while destination in [cup1, cup2, cup3]:
        if destination == 1:
            destination = 9
        else:
            destination -= 1

    # insert the three cups
    x = cups.index(destination)
    if x == len(cups)-1:
        for cup in [cup1, cup2, cup3]:
            cups.append(cup)
    else:
        for cup in [cup3, cup2, cup1]:
            cups.insert(x+1, cup)

    # find next current cup
    x = cups.index(currCup)
    x = (x+1)%len(cups)
    currCup = cups[x]

final = ''
for num in cups:
    final += str(num)
x = final.index('1')
final = final[x+1:] + final[:x]

print(final)

# part 2

class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.nodes = {}

    def insert_left(self, val, prevNode=None) -> Node:
        newNode = Node(val)

        if prevNode is None:
            newNode.next = newNode
            newNode.prev = newNode
        else:
            newNode.prev = prevNode
            newNode.next = prevNode.next
            newNode.prev.next = newNode
            newNode.next.prev = newNode

        self.nodes[val] = newNode
        return newNode

    def pop_right(self, leftNode=None) -> int:
        popNode = leftNode.next
        popVal = popNode.val

        leftNode.next = popNode.next
        popNode.next.prev = leftNode

        del popNode
        del self.nodes[popVal]
        return popVal

    def find(self, val) -> Node:
        return self.nodes[val]

    def get_list(self, marker=1):
        nums = []
        markerNode = self.nodes[marker]
        nums.append(markerNode.val)

        markerNode = markerNode.next
        while markerNode.val != marker:
            nums.append(markerNode.val)
            markerNode = markerNode.next

        return nums

cups = CircularLinkedList()
prevNode = None

for x in data:
    prevNode = cups.insert_left(x, prevNode)
   
for x in range(max(data)+1, 1000001):
    prevNode = cups.insert_left(x, prevNode)

currCup = cups.find(data[0])
for i in range(10000000):
    if i%10000 == 0:
        print(i)
    
    # pick up 3 cups
    cup1 = cups.pop_right(currCup)
    cup2 = cups.pop_right(currCup)
    cup3 = cups.pop_right(currCup)

    # find destination
    if currCup.val == 1:
        x = 1000000
    else:
        x = currCup.val - 1

    while x in [cup1, cup2, cup3]:
        if x == 1:
            x = 1000000
        else:
            x -= 1

    # insert the cups
    destinationCup = cups.find(x)
    for cup in [cup3, cup2, cup1]:
        cups.insert_left(cup, destinationCup)

    del destinationCup

    # update current cup
    currCup = currCup.next

cup1 = cups.find(1)
total = cup1.next.val * cup1.next.next.val
print(total)
