def evenodd(array):
    even=[]
    odd=[]
    for element in range(len(array)):
        if array[element]%2==0:
            even.append(array[element])
        else:
            odd.append(array[element])
    result=even+odd
    return result

array=[3,5,4,22,6,5]
print(evenodd(array))
