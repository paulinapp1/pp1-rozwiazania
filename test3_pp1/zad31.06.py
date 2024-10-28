def f(arr):
    unique=[]
    for element in arr:
        if arr.count(element)==1:
            unique.append(element)

            
    return unique


print(f([2,3,2,5,8,1,9,8]))