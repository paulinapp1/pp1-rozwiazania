integer_array = [2, 5, 8, 11, 14, 17, 20, 23]

# Initialize counters
even_count = 0
odd_count = 0

# Iterate through the array using a while loop
index = 0
while index < len(integer_array):
    # Check if the current element is even or odd and update counters
    if integer_array[index] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    
    # Move to the next element in the array
    index += 1

# Display the results
print("Number of even values in the array:", even_count)
print("Number of odd values in the array:", odd_count)