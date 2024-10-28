def f(arr):
    count = 0 
    for i in arr:
        if arr.count(i) == 1:
            count += 1
    return count
            
print(f([11,22,11,11,22,35,27,11,22,14]))
