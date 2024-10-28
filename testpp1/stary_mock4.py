def f(dictionary,x,y):
    total=0
    for value in dictionary.values():
        for single in value:
         if single>=x  and single<=y:
            total+=int(single)
    return total

print(f({"arr1":[4,5,6], "arr2":[7,5]}, 5, 6) )
