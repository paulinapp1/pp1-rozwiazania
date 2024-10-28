def f(arr2d):
    sums=[]
    suma=0
    for i in range(len(arr2d[0])):
        for j in range(len(arr2d)):
            suma+=arr2d[j][i]
        if suma not in sums:
            sums.append(suma)
            suma=0
        else:
            return True
    return False

print(f([[3,4],[5,1],[4,7]]))
        




    
    
    



