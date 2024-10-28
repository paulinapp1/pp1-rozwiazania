def f(d,v):
    result=0
    for value in d.values():
        if value!=v:
            result+=1
    return result

print(f({"a":True,"b":False,"c":False}, True))