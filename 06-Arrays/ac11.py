def bubble_sort(array):
    n = len(array)

    # Traverse through all array elements
    for i in range(n - 1):
        # Last i elements are already in place, so no need to check them again
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array