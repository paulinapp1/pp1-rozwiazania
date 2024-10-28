def create_2d_arr(x, y):
    return [[0 for _ in range(y)] for _ in range(x)]

# Create a 3x5 two-dimensional array filled with zeroes
created_array = create_2d_arr(3, 5)

print(created_array)