def f(array):
    result=[]
    for i in range(len(array)):
        for j in range(len(array)):
            result.append(array[i][j])
    return result

print(f([[2,3],[1,5]]))
