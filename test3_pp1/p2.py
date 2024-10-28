def f(x,y,digit):
    counter=0
    for i in range(x,y+1):
        number=str(i)
        counter+=number.count(str(digit))
        
    return counter

print(f(10,15,1))