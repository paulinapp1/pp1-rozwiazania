def f(arr):
    for num in arr:
        if arr.count(num)%2!=0:
            return num


print(f([3,3,4,4,4,2,2,2,2]))
print(f([6,6,6,6,4,4,5,2,2,2,2]))