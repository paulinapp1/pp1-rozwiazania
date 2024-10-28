import random
def rand_elem(array):
    return random.choice(array)
my_array = [1, 5, 9, 3, 7, 11, 15]

# Display a few randomly selected array elements
for i in range(3):  # Display three randomly selected elements
    random_element = rand_elem(my_array)
    print("Randomly selected element:", random_element)