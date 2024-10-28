def f(d):
    result=[]
    for row in d:
        for column in row:
            result.append(column)
    return result

a=[[2,3],[1,5]]
print(f(a))

