array=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for i in range(len(array)):
    for j in range(len(array)):
        array[i][j]=(i+1)*(j+1)

for row in array:
    print(row)

print(array[1][2])