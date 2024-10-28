# Initialize the initial array (3x5)
array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

# Display the initial array
print("Initial Array:")
for row in array:
    print(row)

# Swap the first and last columns
for row in array:
    row[0], row[-1] = row[-1], row[0]

# Display the array after swapping columns
print("\nArray after swapping first and last columns:")
for row in array:
    print(row)
