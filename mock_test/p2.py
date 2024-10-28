def f(arr):
    for number in range(len(arr)):
        if arr[number]!=arr[number+1]:
            return arr[number+1]
        

arr=[7,7,7,7,5,7,7,7]
print(f(arr))