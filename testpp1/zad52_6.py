def f(array):
    for row in range(len(array)):
        array[row][0], array[row][-1]= array[row][-1], array[row][0]
