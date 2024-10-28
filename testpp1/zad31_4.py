def f(x,y):
    counter=0
    for number in range(x,y):
        if number<0 and number%2==0:
            counter+=1
    return counter

print(f(-1,11))