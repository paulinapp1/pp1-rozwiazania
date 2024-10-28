def f(n,t):
    counter=0
    for val in t:
        if val==n:
            counter+=1
    return counter

print(f(10,(10,10,50,30)))
