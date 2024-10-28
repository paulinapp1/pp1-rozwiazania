fib=[0,1]
while len(fib)<20:
    n=fib[-1]+fib[-2]
    fib.append(n)
print(fib)
    