array=[
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]

for i in range(len(array)):
    array[i][0], array[i][-1] = array[i][-1], array[i][0]


print(array[0])