def f(expression):
    list_ex=expression.split()
    stack=[]
    for thing in list_ex:
        if thing.isdigit():
            stack.append(int(thing))
        elif thing=="+":
            stack.append(stack.pop()+stack.pop())
        elif thing=="*":
            stack.append(stack.pop()*stack.pop())
        elif thing=="-":
            a,b=stack.pop(), stack.pop()
            stack.append(b-a)
        elif thing=="/":
            a,b=stack.pop(),stack.pop()
            stack.append(int(b/a))
        result=stack[0]
    return result
    
print(f("2 3 + = "))
        
