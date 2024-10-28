def f(arr1,arr2):
    for i in range(len(arr1)):
        if arr1[i]!=arr2[i]:
            return False
    return True
            
    
print(f([3,2,1],[1,2,3]))
        
