def f(x,y,d):
    for i in range(x,y):
        number=str(i)
        if number.count(d)>1:
            return True
    return False

print(f(10,15,"14"))
    