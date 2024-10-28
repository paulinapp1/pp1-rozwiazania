# Define a 2x4 two-dimensional array (list of lists)
two_d_array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

# Display array values in rows and columns
for row in two_d_array:
    for value in row:
        print(value, end=' ')  # Display each value followed by a tab (\t) for spacing
    print()  # Move to the next line for the next row
