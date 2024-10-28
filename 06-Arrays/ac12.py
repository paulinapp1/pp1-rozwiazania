def display_unique(array):
    unique_elements = []
    for i in array:
        if array.count(i)==1:
            unique_elements.append(i)
          

    return unique_elements


array=[2,3,2,5,8,1,9,8]
print(display_unique(array))