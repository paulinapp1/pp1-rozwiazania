def f(arr):
    location_row=0
    location_column=0
    small=10000
    big=0
    for row in range(len(arr)):
        for column in range(len(arr[row])):
            if arr[row][column]>big:
                big=arr[row][column]
                location_row=row
                location_column=column
    return location_column, location_row, big

arr=[[-38, 19], 
     [5,40],
     [-7,11],
     [29,16]]
print(f(arr))
