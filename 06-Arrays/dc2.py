my_array = [1, 2, 3, 4, 5]

# a. Subtract one from the first element of the array
my_array[0] -= 1
print("a. Array after subtracting one from the first element:", my_array)

# b. Increase the last array element by 4
my_array[-1] += 4
print("b. Array after increasing the last element by 4:", my_array)

# c. Multiply the middle array element by 2
middle_index = len(my_array) // 2
my_array[middle_index] *= 2
print("c. Array after multiplying the middle element by 2:", my_array)

# d. Add 3 to each value of the array using a loop
for i in range(len(my_array)):
    my_array[i] += 3

print("d. Array after adding 3 to each element using a loop:", my_array)
