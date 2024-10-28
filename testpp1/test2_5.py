def f(array2D):
    count=0
    for row in array2D:
        if row[0]**2==row[1]:
            count+=1

    return count

print(f([[4,15],[3,9],[-3,-9]]))