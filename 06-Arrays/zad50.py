array=[[-38, 19],
        [5,40],
        [-7,11],
        [29,16]]
smallest=float('inf')
largest=0
column_largest=0
column_smallest=0
row_largest=0
row_smallest=0
for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j]>largest:
            largest=array[i][j]
            column_largest=i
            row_largest=j
        if array[i][j]<smallest:
            smallest=array[i][j]
            column_smallest=i
            row_smallest=i
        

print(largest, column_largest, row_largest)
print(smallest, column_smallest, row_smallest)


