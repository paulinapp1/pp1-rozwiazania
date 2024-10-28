def identity_matrix(n):
    matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:  # Check if the indices are on the diagonal
                matrix[i][j] = 1

    return matrix

print(identity_matrix(3))

