def f(array2D):
    # Initialize column sums list with zeros
    column_sums = [0] * len(array2D[0])

    # Sum elements column-wise
    for row in array2D:
        for col_idx, value in enumerate(row):
            column_sums[col_idx] += value

    return column_sums



print(f([ [3,6,2,7], 
         [9,5,4,0], 
         [2,8,0,9] ]) )
        

