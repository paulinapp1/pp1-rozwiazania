def transpose_matrix(m):
    num_rows = len(m)
    num_cols = len(m[0])

    transposed = [[0 for i in range(num_rows)] for j in range(num_cols)]

    for i in range(num_rows):
        for j in range(num_cols):
            transposed[j][i] = m[i][j]

    return transposed
matrice=[[5,6,7,8]]
tm1=transpose_matrix(matrice)
for row in tm1:
    print(row)