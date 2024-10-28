def f(arr1,arr2):
    counter=0
    for element in arr1:
        if element in arr2:
            counter+=1
    if counter==len(arr2):
        return True
    else:
        return False
    
print(f([1,2,3,4,5,6,7],[1,2,3,4,5]))

    
