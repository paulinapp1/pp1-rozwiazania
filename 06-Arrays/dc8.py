my_array = [[3, 9, 2], [2, 4, 5], [7, 1, 6], [0, 4, 8]]

# Initialize the sum of even numbers
even_sum = 0

# Iterate through the array and calculate the sum of even numbers
for row in my_array:
    for element in row:
        if element % 2 == 0:
            even_sum += element

# Display the result
print(f"The sum of all even numbers in the array is: {even_sum}")