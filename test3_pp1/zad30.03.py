def f(time):
    result=''
    splitted = list(map(int, time.split(':')))
    if splitted[0]<=12:
        result+=time+"am"
    elif splitted[0]>=12:
        result+=str(splitted[0]-12)+":"+str(splitted[1])+'pm'
    return result

print(f("16:32"))