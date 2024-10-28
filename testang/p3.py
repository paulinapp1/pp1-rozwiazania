def f(arr2D):
    arr2D[0], arr2D[-1]=arr2D[-1], arr2D[0]
    return arr2D


print(f([[1,2],[3,4]]))
print(f([[1,2,3,4],[5,6,7,8]]))