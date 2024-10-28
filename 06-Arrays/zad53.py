def identity_matrix(n):
    # Create an empty matrix of size n x n
    result = [[0 for i in range(n)] for j in range(n)]
    
    for i in range(n):
        result[i][i] = 1
        
    
    return result

#identity=identity_matrix(3)
#for row in identity:
 #   print(row)