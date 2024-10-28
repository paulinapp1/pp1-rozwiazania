def f(uid):
    for id in range(1,len(uid)):
        if uid[id-1]==uid[id]:
            return False
    return True

print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]) )
print(f(["bob2","bob2"]))