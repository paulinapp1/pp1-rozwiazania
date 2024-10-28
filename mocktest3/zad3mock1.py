def f(uid):
    visited = set()
    for id in uid:
        if id in visited:
            return False
        visited.add(id)
    return True


print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]) )
print(f(["abc123","ann","abc123","a10"]) )
print(f(["bob2","bob2"]) )
print(f(["bob2","BOB2"]) )