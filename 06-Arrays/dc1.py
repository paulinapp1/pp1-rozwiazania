arr=[2,3,7,5,4]
print(arr)
print(len(arr))
print(arr[0])
print(arr[1])
print(arr[-1])
print(arr[-2])
print(arr[0]+arr[-1])
print(arr[2])
for value in arr:
    print(value, end=" ")
print()
middle_index = len(arr) // 2
for i in range(middle_index + 1):  
    print(arr[i], end=" ") 