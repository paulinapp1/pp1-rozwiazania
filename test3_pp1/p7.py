def f(arr2D):
    total_sum=0
    sums=[]
    for i in range(len(arr2D[0])):
        for j in range(len(arr2D)):
            total_sum+=arr2D[j][i]
        if total_sum not in sums:
            sums.append(total_sum)
            total_sum=0
        else:
            return True
    return False

# Test case
print(f([[3, 4, 2],
         [5, 1, 6]]))
