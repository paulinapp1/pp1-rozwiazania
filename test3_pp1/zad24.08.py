def f(dec):
    stack=[]
    while dec>0:
        stack.append(dec%2)
        dec//=2
    binary=""
    while stack:
        binary+=str(stack.pop())
    return binary
print(f(18))