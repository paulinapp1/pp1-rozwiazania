# Define the array
my_array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Replace the values of the main diagonal with 1 using a loop
for i in range(len(my_array)):
    my_array[i][i] = 1

# Display the modified array
print("\nModified array:")
for row in my_array:
    for element in row:
        print(element, end=" ")
    print()
