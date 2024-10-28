arr=[[3,9,2],
     [2,4,5],
     [7,1,6],
     [0,4,8]]
flat=[]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        flat.append(arr[i][j])
filtered=list(filter(lambda element:element%2!=0,flat))
sum_odd=sum(filtered)
print(sum_odd)

