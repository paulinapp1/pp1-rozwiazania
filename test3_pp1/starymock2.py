def f(arr):
    for number in range(len(arr)):
        if arr[number]!=arr[number+1]:
            return arr[number+1]
        

print(f([7,7,7,5,7,7,7,7]))