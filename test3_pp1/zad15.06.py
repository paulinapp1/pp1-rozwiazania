arr = [[1, 3, 4], [8, 7, 2]]

# Calculate sum of elements at indices (0,2) and (1,2)
sum1 = arr[0][2] + arr[1][2]
print(sum)  # Output: 6

# Calculate sum of elements at indices (0,1) and (1,1)
sum2 = arr[0][1] + arr[1][1]
print(sum2)  # Output: 10

# Calculate sum of elements in the last row
last_row = arr[-1]
sum3 = sum(last_row)
print(sum3)  # Output: 17
