array= [[-38, 19], 
        [40,5],
        [-7,11],
        [29,16]]
row_max=0
column_max=0
row_min=0
column_min=0
max=0
min=100000
for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j]>max:
            max=int(array[i][j])
            row_max=i
            column_max=j
        if array[i][j]<min:
            min=int(array[i][j])
            row_min=i
            column_min=j

print(column_min, row_min, min)
print(column_max,row_max, max)

