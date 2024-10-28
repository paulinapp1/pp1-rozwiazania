def f(n):
    listed=list(str(n))
    list2=[]
    for element in listed:
        list2.append(int(element))
        
    result1=list(filter(lambda x:x%2!=0,list2))
    
    if result1:
       return max(result1)-min(result1)
    else:
        return -1
    
print(f(846206))
        
    
