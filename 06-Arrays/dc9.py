# Define the array
my_array = [[True, False], [True, True], [False, False]]


# Change values to their opposites using a loop
for i in range(len(my_array)):
    for j in range(len(my_array[i])):
        my_array[i][j] = not my_array[i][j]

# Display the modified array
print("\nArray with values changed to their opposites:")
for row in my_array:
    print(row)
