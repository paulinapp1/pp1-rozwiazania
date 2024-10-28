def bubblesort(array):
    n=len(array)
    for i in range(n):
        for j in range(0,n-i-1):
            if array[j]>array[j+1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

myarray=[9,0,4,55,6,3,2]
print(bubblesort(myarray))


