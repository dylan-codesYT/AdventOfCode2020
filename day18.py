
with open('input18.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]

def eval(num1,num2,op):
    if op == '+':
        return num1+num2
    elif op == '*':
        return num1*num2

# sample: 6
def simplify(expr):
    while len(expr) > 1:
        num1 = int(expr.pop())
        op = expr.pop()
        num2 = int(expr.pop())
        result = eval(num1,num2,op)
        expr.append(str(result))
    
    return expr[0]

total = 0
for line in data:
    line = line.replace('(', '( ')
    line = line.replace(')', ' )')
    expr = line.split()

    stack = []

    # expr (list): 3+4*(1*2)
    # stack (stack): 2*4+3
    # ordered: 2
    for ch in expr:
        if ch.isdigit() or ch in ['*', '+', '(']:
            stack.append(ch)

        elif ch == ')':
            ordered = []
            while stack[len(stack)-1] != '(':
                ordered.append(stack.pop())
            stack.pop()

            result = simplify(ordered)
            stack.append(result)

    stack.reverse()
    result = simplify(stack)
    total += int(result)
    
print(total)

# part 2
# 3+4*2
def simplify_with_precedence(expr):
    while len(expr) > 1:
        ordered, hold = [], []
        done = False

        while not done and len(expr) > 0:
            ch = expr.pop()
            if ch == '+':
                done = True
            hold.append(ch)
        
        if len(expr) == 0 and not done:
            result = simplify(hold)
            expr.append(result)

        else:
            ordered.append(expr.pop())
            for _ in range(2):
                ordered.append(hold.pop())
            
            result = simplify(ordered)
            hold.append(result)

            while len(hold) > 0:
                expr.append(hold.pop())

    return expr[0]


total = 0
for line in data:
    line = line.replace('(', '( ')
    line = line.replace(')', ' )')
    expr = line.split()

    stack = []

    for ch in expr:
        if ch.isdigit() or ch in ['*', '+', '(']:
            stack.append(ch)

        elif ch == ')':
            ordered = []
            while stack[len(stack)-1] != '(':
                ordered.append(stack.pop())
            stack.pop()

            result = simplify_with_precedence(ordered)
            stack.append(result)

    stack.reverse()
    result = simplify_with_precedence(stack)
    total += int(result)

print(total)
            