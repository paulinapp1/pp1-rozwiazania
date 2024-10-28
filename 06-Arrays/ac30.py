array = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

# Iterating through the rows of the array
for i, row in enumerate(array):
    # 'i' stores the index of the current row
    # 'row' contains the elements of the current row
    
    # Iterating through the elements of the current row
    for j, val in enumerate(row):
        # 'j' stores the index of the current element in the row
        # 'val' contains the value of the current element
        
        # Within this loop, we're examining each individual element in the array
        # and comparing it with the current minimum and maximum values found so far.
        # The goal is to update the minimum and maximum values and their indices
        # if a smaller minimum or larger maximum value is encountered.
        
        # Check if the current value is smaller than the current minimum value found
        if val < min_value:
            # If yes, update the minimum value and its indices
            min_value = val
            min_row, min_col = i, j
        
        # Check if the current value is larger than the current maximum value found
        if val > max_value:
            # If yes, update the maximum value and its indices
            max_value = val
            max_row, max_col = i, j

# After iterating through the entire array,
# the variables min_value, max_value, min_row, min_col, max_row, and max_col
# store the smallest and largest values and their respective row and column indices.
