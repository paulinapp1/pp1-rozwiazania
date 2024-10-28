def transpose_matrix(m):
    # Get the dimensions of the original matrix
    rows = len(m)
    cols = len(m[0])

    # Create a new matrix to store the transposed elements
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    # Iterate through the original matrix and populate the transposed matrix
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = m[i][j]

    return transposed


a=[[1,2,3],[4,5,6],[7,8,9]]

print(transpose_matrix(a))
    
    