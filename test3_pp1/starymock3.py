def f(array2D):
    row_sums=[]
    col_sums=[]
    row_sum=0
    col_sum=0
    for row in array2D:
        row_sum=0
        for element in row:
            row_sum+=element
        row_sums.append(row_sum)
    for column in range(len(array2D)):
        col_sum=0
        for element in range(len(array2D)):
            col_sum+=array2D[element][column]
        col_sums.append(col_sum)
    for i in range(len(array2D)):
        if row_sums[i]!=col_sums[i]:
            return False
    return True

print(f([[3,7,2],[4,2,5],[5,2,1]]) )
print(f([[3,7,2],[4,2,5],[9,2,1]]) )

        
        



