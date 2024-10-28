def f(array2D):
    sum_rows = [sum(row) for row in array2D]  # Calculate sum of each row

    # Calculate sum of each column
    sum_columns = [sum(array2D[row][col] for row in range(len(array2D))) for col in range(len(array2D))]

    # Check if sums of rows and columns match for each index
    for i in range(len(array2D)):
        if sum_rows[i] != sum_columns[i]:
            return False

    return True




print( f([[3,7,2],[4,2,5],[9,2,1]]) )

