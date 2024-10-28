def onp(expression):
    stack = []
    listex = expression.split()
    
    for thing in listex:
        if thing.isdigit():
            stack.append(int(thing))
        elif thing == "+":
            stack.append(stack.pop() + stack.pop())
        elif thing == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif thing == "*":
            stack.append(stack.pop() * stack.pop())
        elif thing == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))  # Use int() to get integer division
            
    result = stack[0]
    return result

print(onp("2 3 + ="))  # Example test case: 2 + 3 = should output 5

